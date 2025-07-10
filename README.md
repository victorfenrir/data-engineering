# Data Engineering 

Welcome to the data engineering project!

## Prerequisites

Before getting started, you will need to install the following software on your machine:

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
* [VSCode](https://code.visualstudio.com/)

Since the installation process depends on your operating system, you’ll need to handle this part on your own.
However, I've added some guidance for [Windows](./_support/windows.md) and [macOS](./_support/macos.md).

You also need to create a GitHub account to follow along with the project. Create your account at [https://github.com/](https://github.com/).

## Cloning the Project Repository

First, you need to access the original project repository at https://github.com/weslleymoura/data-engineering and create a **fork**. This will make a copy of the project in your own GitHub account (as a new repository).

<img src="_support/git-fork.png" width="400">

**After forking**, open your terminal and navigate to the **directory where you want to save the project** (throughout the project, we will refer to this directory as the **working dir**).

Next, clone your forked project:

```
git clone <<your-repository-url>>
```

To get your project URL, go to the GitHub repository you just forked (in your GitHub account) and copy the following address (HTTPS):

<img src="_support/git-clone.png" width="400">


## Starting the project

Please, execute the following commands to initiate the project.

#### Working directory

Before you start, make sure you are inside the project directory (data-engineering).

#### Build all services

Use the following command to build all services.

```
docker-compose up -d --build
```

ONLY FOR REFERENCE, DO NOT EXECUTE.

You can use the following command to destroy all services.

```
docker-compose down --volumes --remove-orphans
```

In case you have lost refence to the existing containers, it is possible to force a shut down.

```
docker container kill $(docker container ls -q)
```

#### Initial setup of the data catalog

```
docker exec -it spark-master bash -c "/scripts/update_hive_metastore.sh"
```

#### Checking if everyting is okay

Your project is correct if you are able to access the following links from your localhost.

```
MinIO Console UI
http://localhost:9001

Airflow Web UI
http://localhost:8080

Spark Master UI
http://localhost:8081

Apache Superset UI
http://localhost:8088
```

END OF PROJECT INITIATIZATION

## Project configurations

Please, take note of the following project configurations (no need to execute anything).

#### Superset connection string

Use this connection string to connect Superset to the lakehouse.

```
hive://spark-thrift-server:10000/default
```

#### Initiating DBT Docs server

```
docker exec -it airflow bash -c "cd /dbt_lakehouse/target && python3 -m http.server 8091"
```

Check results at http://localhost:8091


## Support commands

#### Access airflow container as root user.

```
docker exec -u 0 -it airflow bash
```

#### Adjust system permissions

For example, if you need to grant full access on airflow folder.

```
chmod -R 777 airflow/
```

#### Run DBT project from Airflow container
```
docker exec -it airflow bash -c "dbt run --project-dir /dbt_lakehouse"
```

#### Run DBT model from Airflow container
```
docker exec -it airflow bash -c "dbt run --project-dir /dbt_lakehouse --select models/marts/fct_summary.sql"
```

#### Connecting to the Hive metastore from spark-master

```
docker exec -it spark-master bash
beeline -u jdbc:hive2://spark-thrift-server:10000
show schemas;
show tables in default;
show tables in marts;
```