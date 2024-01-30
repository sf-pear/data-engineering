What we will be doing in this part of the course:
- How to use docker to run [Postgres](https://www.postgresql.org) with [Mage](https://www.mage.ai)
- Project: using the yellow cab dataset 🚕
  - extract the data
  - transform (clean, transform and partition)
  - load to postgres from Mage
  - load to google cloud storage
  - more transformation using: [pandas](https://pandas.pydata.org), [apache arrow](https://arrow.apache.org), SQL then load to [Google BigQuery](https://cloud.google.com/bigquery)
- Go through how to set up [Google Cloud Storage](https://cloud.google.com/storage/?hl=en) and BigQuery

## What is orchestration?
*"Orchestration is a process of dependency management, facilitated through **automation**."*

Basic idea: we want to minimise manual work.

A data orchestrator will manage:
- scheduling
- triggering
- monitoring
- resource allocation

Orchestration requires sequential steps. These workflows are also called **DAGs** (directed acyclic graphs) or pipelines.

## What is Mage?

*"An open-source pipeline tool for orchestrating, transforming, and integrating data"*

Project(Pipelines(Blocks))

### Project
-A project forms the basis for all the work you can do in Mage— you can think of it like a GitHub repo. 
- It contains the code for all of your pipelines, blocks, and other assets.
- A Mage instance has one or more projects

### Pipelines
- A pipeline is a workflow that executes some data operation— maybe extracting, transforming, and loading data from an API. They’re also called DAGs on other platforms
- In Mage, pipelines can contain Blocks (written in SQL, Python, or R) and charts. 
- Each pipeline is represented by a YAML file in the “pipelines” folder of your project.

### Blocks
- A block is a file that can be executed independently or within a pipeline. 
- Together, blocks form Directed Acyclic Graphs (DAGs), which we call pipelines. 
- A block won’t start running in a pipeline until all its upstream dependencies are met.

They contain several parts:
- Imports
- Function
- Assertion/Test

**It always returns a dataframe.**

## Setting up Mage with Docker

Instead of cloning the whole [repo](https://github.com/mage-ai/mage-zoomcamp/tree/master), I just copied the relevant files to ``.
1. Rename `dev.env` to `.env`
2. Add the `.env` file to `.gitignore`
3. Run `docker compose build`
4. Star the containers `docker compose up`
5. Access Mage GUI on http://localhost:6789

To update mage: `docker pull mageai/mageai:latest` (can take a couple of minutes for slow connections)

## Building a simple pipeline with Mage

💡 When two blocks are connected it means the dataframe outputted from one block will be moving to the next as input.