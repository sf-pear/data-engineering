- [Instructions](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/03-data-warehouse/homework.md)
- [Submission form](https://courses.datatalks.club/de-zoomcamp-2024/homework/hw3)

**Due date**: Feb. 12, 2024, 11 p.m.

# Assignment

Get green taxi data from: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

- [ ] Create an external table using the Green Taxi Trip Records Data for 2022.
- [ ] Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table). 

What I did, using Mage:
1. Created a data loader and got all green taxi 2022 data
2. Uploaded the data to GCS.

# Questions

## 1
Question 1: What is count of records for the 2022 Green Taxi Data?
- [ ] 65,623,481
- [x] 840,402
- [ ] 1,936,423
- [ ] 253,647

**Answer:** I got the answer by looking at how many rows were loaded in Mage. Can also check the "DETAILS" tab for the tables in BigQuery, or do a `SELECT COUNT(*)` query.

## 2
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.

What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- [x] 0 MB for the External Table and 6.41MB for the Materialized Table
- [ ] 18.82 MB for the External Table and 47.60 MB for the Materialized Table
- [ ] 0 MB for the External Table and 0MB for the Materialized Table
- [ ] 2.14 MB for the External Table and 0MB for the Materialized Table

```sql
SELECT COUNT(DISTINCT PULocationID) AS distinct_count
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_external`;

SELECT COUNT(DISTINCT PULocationID) AS distinct_count
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_native`;
```

## 3

How many records have a fare_amount of 0?
- [ ] 12,488
- [ ] 128,219
- [ ] 112
- [x] 1,622

```sql
SELECT COUNT(*) fare_amount
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_external`
WHERE fare_amount = 0
```

## 4

What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? 
- [ ] Cluster on lpep_pickup_datetime Partition by PUlocationID
- [x] Partition by lpep_pickup_datetime Cluster on PUlocationID
- [ ] Partition by lpep_pickup_datetime and Partition by PUlocationID
- [ ] Cluster on by lpep_pickup_datetime and Cluster on PUlocationID
 
Create a new table with this strategy.
```sql
-- create new table with converted date ints to timastamp
-- without this we can partion on time 
CREATE OR REPLACE TABLE `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime` AS
SELECT 
  *, 
  TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64)) AS pickup_datetime, 
  TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime / 1000 AS INT64)) AS dropoff_datetime
FROM 
  `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_native`;

-- create new table - but portioned and clustered
CREATE OR REPLACE TABLE `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime_partioned`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT *
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime`;
```

## 5
Write a query to retrieve:
- the distinct PULocationID 
- between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.

- [ ] 22.82 MB for non-partitioned table and 647.87 MB for the partitioned table
- [x] 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table
- [ ] 5.63 MB for non-partitioned table and 0 MB for the partitioned table
- [ ] 10.31 MB for non-partitioned table and 10.31 MB for the partitioned table

```sql
SELECT DISTINCT PULocationID
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime_partioned`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT PULocationID
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
```

## 6 
Where is the data stored in the External Table you created?

- [ ] Big Query
- [x] GCP Bucket
- [ ] Big Table
- [ ] Container Registry


## 7
It is best practice in Big Query to always cluster your data:
- [ ] True
- [x] False


## 8 (Bonus: Not worth points)
Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

```sql
SELECT COUNT(*) 
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_native`;
```

**Answer:** I get 0 MB, not sure why.