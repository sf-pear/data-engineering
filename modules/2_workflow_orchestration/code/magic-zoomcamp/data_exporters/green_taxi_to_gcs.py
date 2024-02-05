import pyarrow as pa
import pyarrow.parquet as pq 
import os 


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/enhanced-bonito-411221-42d6c353c42e.json'


bucket_name = 'mage-zoomcamp-sabrinafp'
project_id = 'enhanced-bonito-411221'
table_name = 'green_taxi_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    # read dataframe into pyarrow table
    table = pa.Table.from_pandas(data)

    # defining this object allows automacally access out environment variables
    gcs = pa.fs.GcsFileSystem()

    # write dataset as partitioned parquet in GCS
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )