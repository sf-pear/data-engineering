-- question 2
SELECT COUNT(DISTINCT PULocationID) AS distinct_count
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_external`;

SELECT COUNT(DISTINCT PULocationID) AS distinct_count
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_native`;

-- question 3
SELECT COUNT(*) fare_amount
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_external`
WHERE fare_amount = 0

-- question 4
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

-- question 5
SELECT DISTINCT PULocationID
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime_partioned`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT PULocationID
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_datetime`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

-- question 8
SELECT COUNT(*) 
FROM `enhanced-bonito-411221.green_taxi_2022.green_taxi_2022_native`;