# Data Engineering Zoomcamp

This is my code following the DataTalks [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp).

- [Course app](https://dezoomcamp.streamlit.app)
- [YouTube playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [Cohort specific homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024)
- [Original course repo](https://github.com/DataTalksClub/data-engineering-zoomcamp)

## Deadlines

| Module                                                                                                                      | Start Date | Homework Due | Duration (weeks) | Videos                                   | Notes                                     |
| --------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------ | ---------------- | ---------------------------------------- | ----------------------------------------- |
| [1. Introduction & Prerequisites](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) | 15 Jan     | 25 Jan       | 2                | [📺 x7](#1-introduction-and-prerequisites) | [📝](./modules/1_intro_prereqs/notes.md) |
| 2. Workflow Orchestration                                                                                                   | 29 Jan     | 05 Feb       | 1                | [📺 x16](#2-workflow-orchestration)         | 📝                                       |
| dlt workshop                                                                                                                | 05 Feb     | 15 Feb       | n/a              | 📺                                      | 📝                                       |
| 3. Data Warehouse                                                                                                           | 05 Feb     | 12 Feb       | 1                | 📺                                      | 📝                                       |
| 4. Analytics Engineering                                                                                                    | 15 Feb     | 22 Feb       | 1                | 📺                                      | 📝                                       |
| 5. Batch processing                                                                                                         | 22 Feb     | 04 Mar       | 1.5              | 📺                                      | 📝                                       |
| 6. Streaming                                                                                                                | 04 Mar     | 15 Mar       | 1.5              | 📺                                      | 📝                                       |
| RisingWave workshop                                                                                                         | 04 Mar     | 18 Mar       | n/a              | 📺                                      | 📝                                       |
| Project (attempt 1)                                                                                                         | 18 Mar     | 01 Apr       | 2                | 📺                                      | 📝                                       |
| Project evaluation (attempt 1)                                                                                              | 01 Apr     | 08 Apr       | 1                | 📺                                      | 📝                                       |
| Project (attempt 2)                                                                                                         | 01 Apr     | 15 Apr       | 2                | 📺                                      | 📝                                       |
| Project evaluation (attempt 2)                                                                                              | 15 Apr     | 29 Apr       | 1                | 📺                                      | 📝                                       |


## Prep

Here is a checklist of what you need:
- [ ] Set up virtual environment for python development
- [ ] Install Docker
- [ ] Get Google Cloud account

### Create a python virtual enviroment

I use mamba to manage my virtual environments, see `env.yaml` for requirements (This will be updated as I move through the course).


### Install Docker Desktop

Setting up Docker with Windows 11 and WSL is very easy. Assuming WSL is  already installed, install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on Windows. 
To enable the docker CLI on your distro of choice within WSL, just adjust the settings in Docker Desktop:
- Settings > Resources > WSL integration
- Select the distros where you want to enable it to use `docker` commands.

### Create a Google Cloud account

- [dashboard](https://console.cloud.google.com/welcome)
- [SDK](https://cloud.google.com/sdk/docs/install#linux)

<!-- Before course starts:
- [x] Docker Desktop installed
- [x] Env with python (I use mamba)
- [x] Get a Google Cloud account ([dashboard](https://console.cloud.google.com/welcome))
- [ ] Install Google Cloud [SDK](https://cloud.google.com/sdk/docs/install#linux)
    - Assuming they mean the CLI? Do I really need this?
- [ ] Install [Terraform](https://developer.hashicorp.com/terraform/install?product_intent=terraform) (try [OpenTofu](https://opentofu.org/docs/intro/install/deb/))
    - Can I only install it in my env (`mamba install conda-forge::terraform`)? -->

## Modules

### 1. Introduction and Prerequisites

This section will cover Docker, running postgres and pgAdmin containers, some SQL basics and setting up cloud resources in Google Cloud using Terraform.

#### Videos
- [**1**: Introduction to Docker](https://youtu.be/EYNwNlOrpr0)
- [**2**: Ingesting NY Taxi Data to Postgres](https://youtu.be/2JM-ziJt0WI) 
- [**3**: Connecting pgAdmin and Postgres](https://youtu.be/hCAIVe9N0ow)
- [**4**: Dockerizing the Ingestion Script](https://youtu.be/B1WwATwf-vY)
- [**5**: Running Postgres and pgAdmin with Docker-Compose](https://youtu.be/hKI6PkPhpa0)
- [**6**: SQL Refreshser](https://youtu.be/QEcps_iskgg) #NEXT   
- [**7**: ]()
- [**8**: ]()
- [**9**: ]()
- [**10**: ]()
- [**11**: ]()
- [**12**: ]()
- [**Optional** (if you have issues with pgcli): Optional: Connecting to Postgres with Jupyter and Pandas](https://youtu.be/3IkfkTwqHx4)

### 2. Workflow Orchestration

This section will cover Docker, running postgres and pgAdmin containers, some SQL basics and setting up cloud resources in Google Cloud using Terraform.

#### Videos