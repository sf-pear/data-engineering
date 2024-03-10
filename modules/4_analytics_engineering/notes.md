# Analytics Engineering Overview

Analytics Engineering bridges the gap created by the latest developments in the data domain, including advancements in cloud data warehouses, ETL processes, SQL-first tools, self-service analytics, and data governance.

## ETL vs. ELT
ETL (Extract, Transform, Load)
- More stable and compliant data analysis (why?)
- Higher storage and compute costs (why?)

ELT (Extract, Load, Transform)
- Faster and more flexible data analysis (why?)
- Lower cost and lower maintenance (why?)

## Kimball's Dimensional Modeling
- Prioritises:
  - data understandability by the end user
  - Query performance
- This means the we don't focus in not having redundant data ([3NF](https://www.geeksforgeeks.org/third-normal-form-3nf/))  
- Other approaches: [Bill Inmon](https://www.astera.com/type/blog/data-warehouse-concepts/), [Data vault](https://www.databricks.com/glossary/data-vault)

## Materializations

- **Ephemeral**: don't get saved into disk, they only exist for the duration of the dbt run
- **View**: virtual tables created by dbt that cen be queried like regular tables
- **Table**: physical representations of data that are created and stored in the database
- **Incremental**: a powerful feature of dbt that allow for efficient updates to existing tables. reducing the need for full data refreshes.

# DBT set up

If taxi data is not loaded into the db, do this first.

## dbt Cloud and Google BigQuery

### Loading the data

You can load the data directly from the [market place](https://console.cloud.google.com/marketplace/product/city-of-new-york/nyc-tlc-trips?hl=en&project=enhanced-bonito-411221) like this:

```sql
-- yellow trips
CREATE TABLE `enhanced-bonito-411221.taxi_data.yellow_tripdata` AS
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2019`;

INSERT INTO `enhanced-bonito-411221.taxi_data.yellow_tripdata`
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2020`;

-- green trips
CREATE TABLE `enhanced-bonito-411221.taxi_data.green_tripdata` AS
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2019`;

INSERT INTO `enhanced-bonito-411221.taxi_data.green_tripdata`
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2020`;

-- lookup table
CREATE TABLE `enhanced-bonito-411221.taxi_data.taxi_zone_lookup` AS
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.taxi_zone_geom`

--
```

where:
- `taxi_data` is the dataset (this has to be created before running the queries)
- `yellow_tripdata` and `green_tripdata` are the name of the tables (they will be created by the query)

### Create new dbt project

1. Select BigQuery as the connection
2. Name your project
3. If working in one big repo for the whole course: go to advanced settings and give the path to the subdirectory where you want your project to be
4. Create new branch to work in
5.  

To start the dbt project in dbt Cloud, all you have to do is select BigQuery as the connection type, upload your keys for the project and create/select a gihut repo for the project. I created a new repo here to avoid messing up this one.

## Local dbt core and postgres

- Install dbt: `pip install dbt-postgres`. More info [here](https://docs.getdbt.com/docs/core/pip-install#ubuntudebian).
- Run `dbt init` and follow the prompts to set up the starter project
- Run `dbt debug` to check everything is working.

## Building dbt models
..
