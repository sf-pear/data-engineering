# Module 1: Notes

Setting up Docker, using PostgreSQL in Docker, downloading the datasets (diverges from the pre-recorded video lesson), using SQL to get information on the dataset and setting up Terraform.

# Docker
- build your own image: `docker build -t test:pandas .` 
  - image name is `test`
  - image tag tag is `pandas`
  - `.` look for a Dockerfile in the directory and build it.
- run your new image as container: `docker run -it test:pandas`
- to pass an argument to ap python script being executed when running the container: `docker run -it test:pandas 2021-01-15` where the date is the arg you want to pass to `pipeline.py`.

## postgreSQL in Docker
In WSL and windows, using the commands shown in the video does not work, the container does not have permission to write to the local file system. As a work around you can create a docker volume, in this case I called it `pgadmin`.

First run `docker volume create pgdata` then continue with the command given.

```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

You can see the postgres files in the new volume using Docker Desktop:
![GIF showing docker volume in docker desktop UI](./imgs/docker-volume.gif)

To access the database:
- Install `pgcli` in a virtual environment
- Connect to database: `pgcli -h localhost -p 5432 -u root -d ny_taxi`

## Download the datasets
- `wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz`
- `wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv`

To upload the data we need to install a few packages in the visrtual enviroment:
- `pandas`
- `sqlalchemy`
- `psycopg2`

See [`upload-data.ipynb`](../1_intro_prereqs/code/upload-data.ipynb) for loading data to the postgres database.


## Postgres

Run Postgres and load data as shown in the videos.
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

We will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

- [x] Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)

**How complete task:** 
See jupyter notebook [`upload-data.ipynb`](../1_intro_prereqs/code/upload-data.ipynb)


## PgAdmin
```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```
[Open PgAdmin](http://localhost:8080/) in the browser.

To be able to use the new PgAdmin container with our database in the postgres container, they need to be connected. For that we need to put them in the same network, as by default they are isolated. 


## Put postgres and pgadmin in the same network

1. Create a docker network: `docker network create pg-network`
2. Add network option when running the container:
```
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13
```
3. Run pgadmin in the same network:
```
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    dpage/pgadmin4
```
We can also put these in a docker compose file, that way we don't have to have two different terminals to run the two commands separately.


## Ingestion script 

Instead of manually sending data to postgres from the jupyter notebook, we can use a python script for it. To test the script works:

```
python3 ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db_name=ny_taxi \
    --table_name=green_taxi_trips \
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz
```
Now we are ready to dockerize the data ingestion. After editing the Dockerfile to use the new ingestion script and install the required dependencies, we can build the new image:

```
docker build -t taxi_ingest:v001 .
``` 

After building, we can run the pipeline with the following command:
```
docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=pg-database \
        --port=5432 \
        --db_name=ny_taxi \
        --table_name=green_taxi_trips \
        --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz
```

## Docker Compose

USed to start both containers (postgres and pgadmin) at the same time. Some notes:
- Since they are being generated from `docker-compose` we don't need to specify the network - they will automatically be in the same network.

pgAdmin defines a anonymous volume when using docker compose, to override this behaviour we have to name it in the docker-compose file. We also have to define it under `volumes`. The notation `pgadmin_data: {}` is used to define a named volume without any additional configuration options. Here's a breakdown of what it means:

- `pgadmin_data`: This is the name of the volume. You can refer to this name in the volumes section of your services to use this volume.
- `{}`: These curly braces represent an empty dictionary in YAML. In the context of Docker Compose, it means that you're creating a volume named pgadmin_data with the default settings.

Setting up pgAdmin with a persistent volume also persists the settings, so you don't have to create a new server each time you restart the containers.

# Terraform