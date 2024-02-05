- [Instructions](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/02-workflow-orchestration/homework.md)
- [Submission form](https://courses.datatalks.club/de-zoomcamp-2024/homework/hw2)

**Due date**: Feb. 5, 2024, 11 p.m.

# Assignment

The goal will be to construct an ETL pipeline that loads the data, performs some transformations, and writes the data to a database (and Google Cloud!).

- Create a new pipeline, call it `green_taxi_etl`
- Add a data loader block and use Pandas to read data for the final quarter of 2020 (months `10`, `11`, `12`).
  - You can use the same datatypes and date parsing methods shown in the course.
  - `BONUS`: load the final three months using a for loop and `pd.concat`
- Add a transformer block and perform the following:
  - Remove rows where the passenger count is equal to 0 _or_ the trip distance is equal to zero.
  - Create a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date.
  - Rename columns in Camel Case to Snake Case, e.g. `VendorID` to `vendor_id`.
  - Add three assertions:
    - `vendor_id` is one of the existing values in the column (currently)
    - `passenger_count` is greater than 0
    - `trip_distance` is greater than 0
- Using a Postgres data exporter (SQL or Python), write the dataset to a table called `green_taxi` in a schema `mage`. Replace the table if it already exists.
- Write your data as Parquet files to a bucket in GCP, partioned by `lpep_pickup_date`. Use the `pyarrow` library!
- Schedule your pipeline to run daily at 5AM UTC.

# Questions

## Question 1. Data Loading

Once the dataset is loaded, what's the shape of the data?

- [x] 266 855 rows x 20 columns
- [ ] 544 898 rows x 18 columns
- [ ] 544 898 rows x 20 columns
- [ ] 133 744 rows x 20 columns

```py
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):

    data_types={
        'store_and_fwd_flag': str, 
        'RatecodeID': pd.Int64Dtype(),
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'payment_type': pd.Int64Dtype(),
        'trip_type': pd.Int64Dtype(),
        'congestion_surcharge': float,
        }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    base_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz"
    final_quarter = ['10', '11', '12']
    dfs = []
    for month in final_quarter:
        url = base_url.format(month=month)
        df = pd.read_csv(url, compression='gzip', dtype=data_types, parse_dates=parse_dates)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'

```

## Data Transformation

```py
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('[Preprocessing] rows with zero passenger_count:', data['passenger_count'].isin([0]).sum())
    print('[Preprocessing] rows with zero trip_distance:', data['trip_distance'].isin([0]).sum())
    
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0.0)]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.rename(columns={'VendorID': 'vendor_id', 'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_laction_id', 'DOLocationID': 'do_laction_id'}, inplace=True)

    # print(data['vendor_id'].value_counts())

    return data


@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance.'

@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passangers.'

@test
def test_vendor_id(output, *args) -> None:
    assert "vendor_id" in output.columns, 'There is no column called vendor_id'
```

### 2

Upon filtering the dataset where the passenger count is greater than 0 _and_ the trip distance is greater than zero, how many rows are left?

- [ ] 544 897 rows
- [ ] 266 855 rows
- [x] 139 370 rows
- [ ] 266 856 rows


### 3

Which of the following creates a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date?

- [ ] `data = data['lpep_pickup_datetime'].date`
- [ ] `data('lpep_pickup_date') = data['lpep_pickup_datetime'].date`
- [x] `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date`
- [ ] `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date()`

### 4

What are the existing values of `VendorID` in the dataset?

- [ ] 1 2 or 3
- [x] 1 or 2
- [ ] 1 2 3 4
- [ ] 1

```py
# added print statement to transformer to check
print(data['vendor_id'].value_counts())
```

### 5

How many columns need to be renamed to snake case?

- [ ] 3
- [ ] 6
- [ ] 2
- [x] 4

Columns: `VendorID`, `RatecodeID`, `PULocationID` and `DOLocationID`

## Question 6. Data Exporting

Once exported, how many partitions (folders) are present in Google Cloud?

- [x] 96
- [ ] 56
- [ ] 67
- [ ] 108
  
Just checked on the console, not sure if there's a smart way to do it.