import pandas as pd
import requests
from io import BytesIO

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):

    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet"
    months = ["{:02}".format(i) for i in range(1, 13)]
    dfs = []

    for month in months:
        url = base_url.format(month=month)
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            df = pd.read_parquet(BytesIO(response.content), engine='auto')
            dfs.append(df)
        else:
            print(f"Failed to download data for month: {month}")


    df = pd.concat(dfs, ignore_index=True)

    df['lpep_pickup_datetime'] = df['lpep_pickup_datetime'].dt.date
    df['lpep_dropoff_datetime'] = df['lpep_dropoff_datetime'].dt.date
    
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
