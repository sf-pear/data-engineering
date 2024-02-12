## Summary of Data Warehouses Lecture

Partinoed data is much faster to process and also cheaper.

### OLTP vs OLAP
- **OLTP (Online Transaction Processing):** Used in backend services for grouping SQL queries and enabling rollback features for failed transactions. It involves fast but small updates and uses normalized data for efficiency.
- **OLAP (Online Analytical Processing):** Designed for analytical purposes, handling large volumes of data for discovering hidden insights. It uses denormalized data to increase productivity for data analysts.

|                     | OLTP                                                                                              | OLAP                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Purpose             | Control and run essential business operations in **real time**                                    | Plan, solve problems, support decisions, discover hidden insights                 |
| Data updates        | Short, fast updates initiated by user                                                             | Data periodically refreshed with scheduled, long-running batch jobs               |
| Database design     | Normalized databases for efficiency                                                               | Denormalized databases **for analysis**                                           |
| Space requirements  | Generally small if historical data is archived                                                    | Generally large due to aggregating large datasets                                 |
| Backup and recovery | Regular backups required to ensure business continuity and meet legal and governance requirements | Lost data can be reloaded from OLTP database as needed in lieu of regular backups |
| Productivity        | Increases productivity of end users                                                               | Increases productivity of business managers, data analysts, and executives        |
| Data view           | Lists day-to-day business transactions                                                            | Multi-dimensional view of enterprise data                                         |
| User examples       | Customer-facing personnel, clerks, online shoppers                                                | Knowledge workers such as data analysts, business analysts, and executives        |

### What is a Data Warehouse?
A data warehouse is an **OLAP** solution **used for reporting and data analysis**, consisting of raw data, metadata, and summaries. It integrates data from multiple sources into a centralized repository, supporting direct access to raw data, summary data, or data marts for different user needs.

### BigQuery as a Data Warehouse Solution
- **Serverless:** Eliminates the need for managing servers or installing database software.
- **Scalability:** Easily scales from gigabytes to petabytes of data.
- **Features:** Supports machine learning through SQL, handles geospatial data, and performs BI queries efficiently.
- **Cost-Effectiveness:** Separates compute and storage, so if your data grows you don't necessarily have to increase the size of the machine just for storage purposes. AS they are sseparated, this come with big cost savings.

### BigQuery Interface and Features
- Provides a clean interface for managing projects, datasets, and tables.
- Supports external tables from sources like Google Cloud Storage.
- Caches data for faster access but allows disabling for consistent results.
- Offers access to open-source public data sets for analysis.

### Pricing Models
- **On-Demand Pricing:** Charges based on the amount of data processed.
- **Flat Rate Pricing:** Offers a fixed number of slots for a monthly fee, suitable for processing large volumes of data.

### Creating and Querying Tables in BigQuery
- Demonstrated how to create external tables from datasets and perform queries.
- Showed the process of transforming external data into BigQuery storage for analysis.

### Partitioning and Clustering in BigQuery
- **Partitioning:** Improves query performance by organizing data into partitions based on specific columns (e.g., date).
- **Clustering:** Further enhances performance and cost-efficiency by grouping data within partitions based on specified columns (e.g., vendor ID).


*Notes only for first video - haven't watched it all. Maybe one day...*
