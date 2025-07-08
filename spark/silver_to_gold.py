from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def run():
    spark = SparkSession.builder.appName("silver_to_gold").master("spark://spark-master:7077") \
        .config("spark.jars.packages", ",".join([
            "io.delta:delta-core_2.12:2.4.0",
            "org.apache.hadoop:hadoop-aws:3.3.4",
            "com.amazonaws:aws-java-sdk-bundle:1.12.262"
        ])) \
        .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minio") \
        .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.sql.warehouse.dir", "s3a://gold/warehouse") \
        .enableHiveSupport() \
        .getOrCreate()

    silver_path = "s3a://silver/warehouse/default/sample_data"

    df = spark.read.format("delta").load(silver_path)
    df = df.withColumn("amount", F.col("amount").cast("double"))

    summary = df.groupBy("customer_id").sum("amount").withColumnRenamed("sum(amount)", "total_amount")

    summary.write.format("delta").mode("overwrite") \
        .option("path", "s3a://gold/warehouse/default/order_summary") \
        .option("mergeSchema", "true") \
        .saveAsTable("default.order_summary")

    spark.stop()
