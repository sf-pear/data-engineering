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
- Good to update as they release new versions often.
- After updating you have to rebuild the images.

## Building Your First Pipeline in Mage

- To **build a pipeline** select "New Pipeline" or use the "Pipelines" page for an overview of existing pipelines.
- Projects in Mage contain multiple pipelines. The "Magic Zoom Camp" example project contains an `example_pipeline` demonstrating basic functionality.
  - The example pipeline demonstrates reading from an API, processing data, and exporting it to a local data frame. It includes data loading, transformation, and export blocks.
- The pipeline view shows a file tree of your project and the blocks making up your pipeline. When two blocks are connected it means the dataframe outputted from one block will be moving to the next as input.
- You can execute blocks together or individually.


## Configuring Postgres

How to configure the postgres client so it can connect to the local postgres database in the docker image we built:

1. We define the postgres configuration in [`docker_compose.yml`](./code/docker-compose.yml) - 
2. Sensitive information such as database credentials are defined as environment variables are defined in the `.env` file.
3. Ensure we have a connection to the database from Mage
   1. We can do this in the Mage GUI or in VS code - the file we need here is [`io_config.yaml`](./code/magic-zoomcamp/io_config.yaml)
   
![how to find mage's file tree](./imgs/mage-files.gif)

### Creating connection profiles in mage

You can see in the  file, there is a default profile defined. But we can also define for example a "dev" profile. This is useful to separate configurations needed in dev and in production. 

```yaml
version: 0.1.1
default:
  # Default profile created for data IO access.
  # Add your credentials for the source you use, and delete the rest.
```

In the end of the file you add the following lines to create a new profile.

```yaml
dev:
  POSTGRES_CONNECT_TIMEOUT: 10
  POSTGRES_DBNAME: {{ env_var('POSTGRES_DBNAME') }}
  POSTGRES_SCHEMA: {{ env_var('POSTGRES_SCHEMA') }}
  POSTGRES_USER: {{ env_var('POSTGRES_USER') }}
  POSTGRES_PASSWORD: {{ env_var('POSTGRES_PASSWORD') }}
  POSTGRES_HOST: {{ env_var('POSTGRES_HOST') }}
  POSTGRES_PORT: {{ env_var('POSTGRES_PORT') }}  
```

💡 Mage uses [Jinja](https://jinja.palletsprojects.com) templating for interpolating environment variables (same as dbt) directly within the configuration file.

To test everything is working:
1. Create a new batch pipeline
2. Rename to *test_config*: edit > pipeline settings
3. Add SQL dataloader to pipeline to test the configuration

![Data loader block to test postgres connection](./imgs/dataloader-block.gif)

## API to Postgres

Building a more advanced pipeline that:
- pulls data
- performs a light transformation
- writes to data source

### Step by step
1. Create new bacth pipeline and rename it to `api_to_postgres`.
2. Create [data loader](#data-loader) to fetch data from an URL and load it using pandas (+ Data loader > Python > API)
3. Create [transformer](#transformer) block to clean/transform the data (+ Transformer > Python > Generic)
4. Create data exporter to send transformed data to postgres database (+ Data exporter > Python > PostgreSQL)

#### Data Loader
- We have to **declare** the data types for pandas. Why? Drastically reduces memory usage - makes a huge difference for memory consumption, especially for big datasets like this one (>1 million rows)
- To do this we need to first have a look at the dataset to know what are data types of each featrue in the dataset. 
- We can also explicitly tell pandas which columns include datetime so it can parse it.

Data loading block:
```py
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'
    
    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    # native date parsing 
    parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']

    return pd.read_csv(
        url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates
        )


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
```

#### Transformer

To clean up the data:
- Remove rows with passenger count = 0 (doesn't make sense to have a taxi ride with no pessenger, so we remove the anomalous data)

Data transformation block:
```py
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('Preprocessing: rows with zero passangers:', data['passenger_count'].isin([0]).sum())

    return data[data['passenger_count'] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passangers.'
```

#### Data exporter
Update values for:
- `schema_name`
- `table_name`
- `config_profile`

```py
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """
    schema_name = 'ny_taxi'  # Specify the name of the schema to export data to
    table_name = 'yellow_cab_data'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
```

We can add a data loader to confirm everything worked. I also like using the [PostgreSQL Explorer VS Code extension](https://marketplace.visualstudio.com/items?itemName=ckolkman.vscode-postgres) to have a look at my databases. 

This is how to connect it:

![Connect to database using postgres explorer](./imgs/postgres-explorer.gif)
