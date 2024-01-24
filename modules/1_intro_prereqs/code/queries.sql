
-- get number of records in table
SELECT count(1) FROM green_taxi_trips;


-- get top 3
SELECT * FROM zones LIMIT 3;


-- inner join
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' / ', zpu."Zone") as "pickup_loc",
    CONCAT(zdo."Borough", ' / ', zdo."Zone") as "dropoff_loc"
FROM
    green_taxi_trips t,
    zones zpu,
    zones zdo
WHERE
    t."PULocationID" = zpu."LocationID" AND
    t."DOLocationID" = zdo."LocationID"
LIMIT 100;


-- another version of inner join
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' / ', zpu."Zone") as "pickup_loc",
    CONCAT(zdo."Borough", ' / ', zdo."Zone") as "dropoff_loc"
FROM
    green_taxi_trips t JOIN zones zpu
        ON t."PULocationID" = zpu."LocationID" 
    JOIN zones zdo
        ON t."DOLocationID" = zdo."LocationID"   
LIMIT 100;


-- example of outer join using LEFT JOIN
-- to show records from green_taxi_trips 
-- even if there is no corresponding record in zones  
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' / ', zpu."Zone") as "pickup_loc",
    CONCAT(zdo."Borough", ' / ', zdo."Zone") as "dropoff_loc"
FROM
    green_taxi_trips t JOIN zones zpu
        ON t."PULocationID" = zpu."LocationID" 
    JOIN zones zdo
        ON t."DOLocationID" = zdo."LocationID"   
LIMIT 100;


-- check for records without pickup and dropoff locations
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    "PULocationID",
    "DOLocationID"
FROM
    green_taxi_trips t
WHERE
    "PULocationID" is NULL;


-- any dropoff ids not present in the database?
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    "PULocationID",
    "DOLocationID"
FROM
    green_taxi_trips t
WHERE
    "DOLocationID" NOT IN (SELECT "LocationID" FROM zones)
LIMIT 100;


-- groupby queries
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    DATE_TRUNC('DAY', lpep_dropoff_datetime),
    total_amount,
FROM
    green_taxi_trips t
LIMIT 100;


-- take away time from field and show only date
SELECT 
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    CAST(lpep_dropoff_datetime AS DATE),
    total_amount
FROM
    green_taxi_trips t
LIMIT 100;


-- get count of trips per day and order by date
SELECT 
    CAST(lpep_dropoff_datetime AS DATE) as "day",
    COUNT(1)
FROM
    green_taxi_trips t
GROUP BY
    CAST(lpep_dropoff_datetime AS DATE)
ORDER BY "day" ASC;


-- get count per date and order by count 
-- to find the day with most trips
SELECT 
    CAST(lpep_dropoff_datetime AS DATE) as "day",
    COUNT(1)
FROM
    green_taxi_trips t
GROUP BY
    CAST(lpep_dropoff_datetime AS DATE)
ORDER BY "count" DESC;


-- add some more info to the query
SELECT 
    CAST(lpep_dropoff_datetime AS DATE) as "day",
    COUNT(1),
    MAX(total_amount),
    MAX(passenger_count)
FROM
    green_taxi_trips t
GROUP BY
    CAST(lpep_dropoff_datetime AS DATE)
ORDER BY "count" DESC;


-- groupby 2 fields, date of dropoff and dropoff id
-- order by date and dropoff location id
SELECT 
    CAST(lpep_dropoff_datetime AS DATE) as "day", "DOLocationID",
    COUNT(1),
    MAX(total_amount),
    MAX(passenger_count)
FROM
    green_taxi_trips t
GROUP BY
    1, 2
ORDER BY "day" ASC, "DOLocationID" ASC;
