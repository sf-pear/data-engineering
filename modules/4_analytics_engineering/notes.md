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

# DBT

## Set up

### Local dbt core and portgres

- Install dbt: `pip install dbt-postgres`. More info [here](https://docs.getdbt.com/docs/core/pip-install#ubuntudebian).
- Run `dbt init` and follow the prompts to set up the starter project
- Run `dbt debug` to check everything is working.
- If taxi data is not loaded into teh db, [do that](#loadingreloading-the-data)

## Materializations

- **Ephemeral**: don't get saved into disk, they only exist for the duration of the dbt run
- **View**: virtual tables created by dbt that cen be queried like regular tables
- **Table**: physical representations of data that are created and stored in the database
- **Incremental**: a powerful feature of dbt that allow for efficient updates to existing tables. reducing the need for full data refreshes.

## Loading/Reloading the data
In case you totally forgot how this was done tin the first place (I did) and at this point I only have the green taxi data in my local postgres db.



