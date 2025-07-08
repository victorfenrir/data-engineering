from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import os
import sys

# Make sure the scripts directory is importable
sys.path.append('/app')

from bronze_to_silver import run as bronze_to_silver_run
from silver_to_gold import run as silver_to_gold_run

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1)
}

with DAG('lakehouse_pipeline',
         default_args=default_args,
         #schedule_interval="0 6 * * *",  # daily at 6 AM
         schedule_interval=None,
         catchup=False) as dag:

    start = EmptyOperator(task_id='start')

    #create_trino_table = BashOperator(
    #    task_id='create_trino_table',
    #    bash_command="""
    #    trino --server trino:8080 --catalog gold --schema default --execute "
    #    CREATE TABLE IF NOT EXISTS order_summary (
    #        customer_id VARCHAR,
    #        total_amount DOUBLE
    #    )
    #    WITH (location = 's3a://gold/warehouse/default/order_summary')"
    #    """
    #)

    bronze_to_silver = PythonOperator(
        task_id='bronze_to_silver',
        python_callable=bronze_to_silver_run
    )

    silver_to_gold = PythonOperator(
        task_id='silver_to_gold',
        python_callable=silver_to_gold_run
    )

    end = EmptyOperator(task_id='end')

    start >> bronze_to_silver >> silver_to_gold >> end
