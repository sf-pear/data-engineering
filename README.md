# Data Engineering Zoomcamp

This is my collection of notes and code from following the DataTalks [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp).

- [YouTube playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [Cohort specific homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024)
- [Original course repo](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [Course app](https://dezoomcamp.streamlit.app)

## Deadlines

| Module                                                               | Start Date | Homework Due | Weeks to complete | Videos | Duration | Notes                                              |
| -------------------------------------------------------------------- | ---------- | ------------ | ----------------- | ------ | -------- | -------------------------------------------------- |
| [1. Introduction & Prerequisites](#1-introduction-and-prerequisites) | 15 Jan     | 25 Jan       | 2                 | x9     | 2h 50m   | [📝](./modules/1_intro_prereqs/notes.md)          |
| [2. Workflow Orchestration](#2-workflow-orchestration)               | 29 Jan     | 05 Feb       | 1                 | x11    | 1h 32m   | [📝](./modules/2_workflow_orchestration/notes.md) |
| [dlt workshop](#dlt)                                                 | 05 Feb     | 15 Feb       | 1.5               | x1     | 1h 20m   | [📝](./workshops/dlt/notes.md)                    |
| 3. Data Warehouse                                                    | 05 Feb     | 12 Feb       | 1                 |        |          | 📝                                                |
| 4. Analytics Engineering                                             | 15 Feb     | 22 Feb       | 1                 |        |          | 📝                                                |
| 5. Batch processing                                                  | 22 Feb     | 04 Mar       | 1.5               |        |          | 📝                                                |
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
- Module notes
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
- [Module notes](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration)
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

## Workshops

### dlt
The workshop quickly covers how to build data ingestion pipelines using dlt. It includes:
- ​Extracting data from APIs, or files.
- ​Normalizing and loading data
- ​Incremental loading

#### 📚 Resources
- [Workshop notes](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/workshops/dlt.md)
- Homework
- [dlt docs](https://dlthub.com/docs/intro)
  
#### 📺 Video
- [Data Ingestion From APIs to Warehouses - Adrian Brudaru](https://www.youtube.com/watch?v=oLXhBM7nf2Q)
