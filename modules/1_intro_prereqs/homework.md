# Module 1: Homework Questions 

## Docker

### 1
Which tag has the following text? - *Automatically remove the container when it exits* 

- [ ] `--delete`
- [ ] `--rc`
- [ ] `--rmc`
- [x] `--rm`

**How to answer:** Run `docker run --help` and read the help text for different flags.

#### 2
1. Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
2. Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- [x] 0.42.0
- [ ] 1.0.0
- [ ] 23.0.1
- [ ] 58.1.0

**How to answer:** 
1. Run the container `docker run -it python:3.9` 
2. It will download if you don't have it, 
3. You will see you go directly into python so can't use `pip`, so we have to exit it and access bash in that same container.
4. Run the container again with an entrypoint `docker run -it --entrypoint=bash python:3.9`
5. Now you can run `pip list wheel`

## SQL

### 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- [ ] 15767
- [x] 15612
- [ ] 15859
- [ ] 89009


```sql
SELECT 
    COUNT(1)
FROM
    green_taxi_trips t
WHERE
    CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
    AND
    CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18';
```

### 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- [ ] 2019-09-18
- [ ] 2019-09-16
- [x] 2019-09-26
- [ ] 2019-09-21

```sql
SELECT 
    CAST(lpep_pickup_datetime AS DATE) as "day",
    COUNT(1),
    MAX(trip_distance) as "max distance"
FROM
    green_taxi_trips t
GROUP BY
    CAST(lpep_pickup_datetime AS DATE)
ORDER BY "max distance" DESC;
```

### 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- [x] "Brooklyn" "Manhattan" "Queens"
- [ ] "Bronx" "Brooklyn" "Manhattan"
- [ ] "Bronx" "Manhattan" "Queens" 
- [ ] "Brooklyn" "Queens" "Staten Island"

```sql
SELECT 
    zpu."Borough" as "pickup_borough",
    SUM(total_amount)
FROM
    green_taxi_trips t FULL OUTER JOIN zones zpu
        ON t."PULocationID" = zpu."LocationID"
WHERE
    CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
GROUP BY
    pickup_borough
HAVING
    SUM(total_amount) > 50000;
```


### 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- [ ] Central Park
- [ ] Jamaica
- [x] JFK Airport
- [ ] Long Island City/Queens Plaza

```sql
SELECT 
    CAST(lpep_dropoff_datetime AS date),
    zpu."Zone" as "pickup_zone",
    zdo."Zone" as "dropoff_zone",
    tip_amount
FROM
    green_taxi_trips t 
    FULL OUTER JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
    FULL OUTER JOIN zones zdo ON t."DOLocationID" = zdo."LocationID"
WHERE
    EXTRACT(YEAR FROM lpep_dropoff_datetime) = 2019 AND
    EXTRACT(MONTH FROM lpep_dropoff_datetime) = 9 AND
    zpu."Zone" = 'Astoria'
ORDER BY tip_amount DESC;
```

# Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the `main.tf` and `variable.tf` (this doesn't exist?) files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.


## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw01
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET