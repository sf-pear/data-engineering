# Data Engineering Zoomcamp

This is my collection of notes and code from following the DataTalks [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp).

- [YouTube playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [Cohort specific homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024)
- [Homework submission](https://courses.datatalks.club/de-zoomcamp-2024/)
- [Original course repo](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [Course app](https://dezoomcamp.streamlit.app)

## Deadlines

🗓️ [Project's timeline](https://public.flourish.studio/visualisation/16782770/)

| Module                                                               | Start Date | Homework Due | Weeks to complete | Videos | Duration | Notes                                              |
| -------------------------------------------------------------------- | ---------- | ------------ | ----------------- | ------ | -------- | -------------------------------------------------- |
| 1. [Introduction & Prerequisites](#1-introduction-and-prerequisites) | 15 Jan     | 25 Jan       | 2                 | x9     | 2h 50m   | [📝](./modules/1_intro_prereqs/notes.md)          |
| 2. [Workflow Orchestration](#2-workflow-orchestration)               | 29 Jan     | 05 Feb       | 1                 | x11    | 1h 32m   | [📝](./modules/2_workflow_orchestration/notes.md) |
| 3. [Data Warehouse](#3-data-warehouse)                               | 05 Feb     | 12 Feb       | 1                 | x6     | 1h 01m   | [📝](./modules/3_data_warehouse/notes.md)         |
| [dlt workshop](#dlt)                                                 | 05 Feb     | 15 Feb       | 1.5               | x1     | 1h 20m   | [📝](./workshops/dlt/notes.md)                    |
| 4. [Analytics Engineering](#4-analytics-engineering)                 | 15 Feb     | 22 Feb       | 1                 | x10    | 2h 41m   | [📝](./modules/4_analytics_engineering/notes.md)  |
| 5. [Batch processing](#5-batch-processing)                           | 22 Feb     | 04 Mar       | 1.5               |        |          | 📝                                                |
| 6. Streaming                                                         | 04 Mar     | 15 Mar       | 1.5               |        |          | 📝                                                |
| RisingWave workshop                                                  | 04 Mar     | 18 Mar       | n/a               |        |          | 📝                                                |
| Project (attempt 1)                                                  | 18 Mar     | 01 Apr       | 2                 |        |          | 📝                                                |
| Project evaluation (attempt 1)                                       | 01 Apr     | 08 Apr       | 1                 |        |          | 📝                                                |
| Project (attempt 2)                                                  | 01 Apr     | 15 Apr       | 2                 |        |          | 📝                                                |
| Project evaluation (attempt 2)                                       | 15 Apr     | 29 Apr       | 1                 |        |          | 📝                                                |


## Prep

Here is a checklist of what you need:
- [ ] Set up virtual environment for python development
- [ ] Install Docker Desktop
- [ ] Get [Google Cloud](https://console.cloud.google.com/welcome) account
- [ ] Install Terraform (you can follow the [docs](https://developer.hashicorp.com/terraform/install?product_intent=terraform), or like me, install it in a conda environment)


### Create a python virtual environment

I use mamba to manage my virtual environments, see `env.yaml` for requirements (This will be updated as I move through the course).


### Install Docker Desktop

Setting up Docker with Windows 11 and WSL is very easy. Assuming WSL is already installed, install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on Windows. 
To enable the docker CLI on your distro of choice within WSL, just adjust the settings in Docker Desktop:
- Settings > Resources > WSL integration
- Select the distros where you want to enable it to use `docker` commands.


## Modules

### 1. Introduction and Prerequisites

This section will cover Docker, running postgres and pgAdmin containers, some SQL basics and setting up cloud resources in Google Cloud using Terraform.

#### 📚 Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) 
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/01-docker-terraform/homework.md)

#### 📺 Videos
- [**1**: Introduction to Docker](https://www.youtube.com/watch?v=EYNwNlOrpr0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=4)
- [**2**: Ingesting NY Taxi Data to Postgres](https://www.youtube.com/watch?v=2JM-ziJt0WI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=5) 
- [**3**: Connecting pgAdmin and Postgres](https://www.youtube.com/watch?v=hCAIVe9N0ow&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=7)
- [**4**: Dockerizing the Ingestion Script](https://www.youtube.com/watch?v=B1WwATwf-vY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=8)
- [**5**: Running Postgres and pgAdmin with Docker-Compose](https://www.youtube.com/watch?v=hKI6PkPhpa0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=9)
- [**6**: SQL Refreshser](https://www.youtube.com/watch?v=QEcps_iskgg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=10) 
- [**7**: Terraform Primer](https://www.youtube.com/watch?v=s2bOYDCKl_M&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=11)
- [**8**: Terraform Basics](https://www.youtube.com/watch?v=Y2ux7gq3Z0o&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=12)
- [**9**: Terraform Variables](https://www.youtube.com/watch?v=PBi0hHjLftk&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13)

Bonus videos:
- [Setting up the Environment on Google Cloud](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=14)
- [Using Github Codespaces for the Course](https://www.youtube.com/watch?v=XOSUt8Ih3zA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=15)
- [Port Mapping and Networks in Docker](https://www.youtube.com/watch?v=tOr4hTsHOzU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=16)
- [Optional (if you have issues with pgcli): Connecting to Postgres with Jupyter and Pandas](https://www.youtube.com/watch?v=3IkfkTwqHx4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=6)

### 2. Workflow Orchestration

This section covers workflow orchestration with Mage. 

#### 📚 Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration)
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/02-workflow-orchestration/homework.md)
- [Mage docs](https://docs.mage.ai/introduction/overview)

#### 📺 Videos

- [**1**: What is Orchestration?](https://www.youtube.com/watch?v=Li8-MWHhTbo&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [**2**: What is Mage?](https://www.youtube.com/watch?v=AicKRcK3pa4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=18)
- [**3**: Configure Mage](https://www.youtube.com/watch?v=2SV-av3L3-k&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=19)
- [**4**: A Simple Pipeline](https://www.youtube.com/watch?v=stI-gg4QBnI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=20)
- [**5**: Configuring Postgres](https://www.youtube.com/watch?v=pmhI-ezd3BE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=21) 
- [**6**: API to Postgres](https://www.youtube.com/watch?v=Maidfe7oKLs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=22)
- [**7**: Configuring GCP](https://www.youtube.com/watch?v=00LP360iYvE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=23) 
- [**8**: ETL: API to GCS](https://www.youtube.com/watch?v=w0XmcASRUnc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=24)
- [**9**: ETL: GCS to BigQuery](https://www.youtube.com/watch?v=JKp_uzM-XsM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=25) 
- [**10**: Parameterized Execution](https://www.youtube.com/watch?v=H0hWjWxB-rg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=26)
- [**11**: Backfills](https://www.youtube.com/watch?v=ZoeC6Ag5gQc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=27)

Deployment videos (they say optional, but this is pretty crucial for me):
- [Deployment Prerequisites](https://www.youtube.com/watch?v=zAwAX5sxqsg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=28)
- [Google Cloud Permissions](https://www.youtube.com/watch?v=O_H7DCmq2rA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=29)
- [Deploying to Google Cloud Part 1](https://www.youtube.com/watch?v=9A872B5hb_0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=30)
- There seems to be a missing video here. See [notes](./modules/2_workflow_orchestration/notes.md#terraform-deployment-to-gcp) for details on how to deploy using Terraform.
- [Deploying to Google Cloud Part 2](https://www.youtube.com/watch?v=0YExsb2HgLI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=31)
- [Next Steps](https://www.youtube.com/watch?v=uUtj7N0TleQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=32)

Office hours recording [here](https://www.youtube.com/watch?v=7PBvH6dHVxc).

### 3. Data Warehouse

In this section we will talk about data warehousing in general and use [Google BigQuery](https://cloud.google.com/bigquery) as an example.

#### 📚 Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/03-data-warehouse)
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/03-data-warehouse/homework.md)

#### 📺 Videos
- [**1:** Data Warehouse and BigQuery](https://www.youtube.com/watch?v=jrHljAoD6nM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=35)
- [**2:** Partioning and Clustering](https://www.youtube.com/watch?v=-CqXf7vhhDs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=35)
- [**3:** BigQuery Best Practices](https://www.youtube.com/watch?v=k81mLJVX08w&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=36)
- [**4:** Internals of Big Query](https://www.youtube.com/watch?v=eduHi1inM4s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=37)
- [**5:** BigQuery Machine Learning](https://www.youtube.com/watch?v=B-WtpB0PuG4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=38)
- [**6:** BigQuery Machine Learning Deployment](https://www.youtube.com/watch?v=BjARzEWaznU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=39)


### 4. Analytics Engineering

#### 📚 Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering)
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/04-analytics-engineering/homework.md)

#### 📺 Videos
- [**1:** Analytics Engineering Basics](https://www.youtube.com/watch?v=uF76d5EmdtU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=41)
- [**2:** What is dbt?](https://www.youtube.com/watch?v=gsKuETFJr54&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=41)
- Start Your dbt Project
  - [**3:** BigQuery and dbt Cloud](https://www.youtube.com/watch?v=J0XCDyKiU64&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=42)
  - [**4:** Postgres and dbt Core Locally](https://www.youtube.com/watch?v=1HmL63e-vRs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=43)
- [**5:** Build the First dbt Models](https://www.youtube.com/watch?v=ueVy2N54lyc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=44)
- [**6:** Testing and Documenting the Project](https://www.youtube.com/watch?v=2dNJXHFCHaY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=45)
- Deployment
  - [**7:** Using dbt Cloud ](https://www.youtube.com/watch?v=V2m5C0n8Gro&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=46)
  - [**8:** Using dbt Locally](https://www.youtube.com/watch?v=Cs9Od1pcrzM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=47)
- Visualising the data
  - [**9:** with Google Data Studio](https://www.youtube.com/watch?v=39nLTs74A3E&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=48)
  - [**10:** with Metabase](https://www.youtube.com/watch?v=BnLkrA7a6gM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=49)

Optional:
- [Hack for loading data to BigQuery](https://www.youtube.com/watch?v=Mork172sK_c&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=50)

<!-- 7m 14s + 7m 4s + 5m 19s + 6m 47s + 55m 49s + 21m 8s + 13m 11s + 7m 25s + 20m 1s + 17m 28s  -->

### 5. Batch Processing

#### 📚 Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-batch)
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/05-batch/homework.md)

#### 📺 Videos
- **1:** Introduction to Batch Processing
- **2:** Introduction to Spark
- **3:** First Look at Spark/PySpark
- **4:** Spark Dataframes
- **5:** SQL with Spark
- **6:** Anatomy of a Spark Cluster
- **7:** GroupBy in Spark
- **8:** Joins in Spark

9m 30s + 

Optional:
- [Installing Spark (Linux)](https://www.youtube.com/watch?v=hqUbB9c8sKg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=54)
- [Preparing Yellow and Green Taxi Data](https://www.youtube.com/watch?v=CI3P4tAtru4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=57)
- Resilient Distributed Datasets
  - Operations on Spark RDDs
  - Spark RDD mapPartition
- Running Spark in the Cloud
  - Connecting to Google Cloud Storage
  - Creating a Local Spark Cluster


## Workshops

### dlt
The workshop quickly covers how to build data ingestion pipelines using dlt. It includes:
- ​Extracting data from APIs, or files.
- ​Normalizing and loading data
- ​Incremental loading

#### 📚 Resources
- [Workshop](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/workshops/dlt.md)
- Homework
- [dlt docs](https://dlthub.com/docs/intro)
  
#### 📺 Video
- [Data Ingestion From APIs to Warehouses - Adrian Brudaru](https://www.youtube.com/watch?v=oLXhBM7nf2Q)
