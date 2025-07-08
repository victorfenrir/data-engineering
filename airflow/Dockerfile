FROM apache/airflow:2.9.1

# Install Java
USER root

# Add APT sources and install Java
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    && apt-get clean

# Set JAVA_HOME for PySpark
ENV JAVA_HOME=/usr/lib/jvm/java-1.17.0-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Trino CLI
RUN curl -L https://repo1.maven.org/maven2/io/trino/trino-cli/440/trino-cli-440-executable.jar -o /usr/local/bin/trino && \
    chmod +x /usr/local/bin/trino

USER airflow

# Install Python dependencies: PySpark, DBT
RUN pip install --no-cache-dir \
    pyspark==3.4.3 \
    dbt-core==1.10.3 \
    dbt-trino==1.9.2 \
    dbt-spark==1.9.2 \
    dbt-spark[PyHive]

RUN pip install psycopg2-binary