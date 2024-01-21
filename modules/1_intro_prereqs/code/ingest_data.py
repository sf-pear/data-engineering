import argparse
import os
from time import time

from sqlalchemy import create_engine
import pandas as pd

def main(params):  
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.db_name
    table_name = params.table_name   
    url = params.url
    
    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=10000)

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    
    print("Creating table...")
    print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))
    
    # create table with extracted schema
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    # upload data froem first chunk
    df.to_sql(name=table_name, con=engine, if_exists='append') 

    
    # start uploading the rest of the data in chunks
    row_count = 0

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            row_count += df.shape[0]
            
            # convert tring to datetime
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            t_end = time()
            
            print("Inserted another chunk... it took %.3f second(s)" % (t_end - t_start))
            
        except StopIteration: # catch exception and break gracefully
            break 
        
    print(f"Successfully uploaded {row_count} records to {db_name}.{table_name} table")   


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL.')
    
    parser.add_argument('--user', type=str, help='username for postgres')
    parser.add_argument('--password', type=str, help='password for postgres')
    parser.add_argument('--host', type=str, help='host for postgres')
    parser.add_argument('--port', type=int, help='port for postgres')
    parser.add_argument('--db_name', type=str, help='name of the database')
    parser.add_argument('--table_name', type=str, help='name of the table')
    parser.add_argument('--url', type=str, help='url of the csv file')
    
    args = parser.parse_args()
    
    main(args)

 


