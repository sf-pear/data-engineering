import requests
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

class YellowTaxiLoader:
    def __init__(self, owner, repo, tag, db_config):
        self.url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"
        self.engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    def fetch_assets(self):
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        assets = [asset for asset in data['assets'] if asset['name'].endswith('.csv.gz')]
        return assets

    def load_assets(self, assets):
        first_chunk = True
        for asset in tqdm(assets, desc='Assets', unit='asset'):
            df_iter = pd.read_csv(asset['browser_download_url'], compression='gzip', iterator=True, chunksize=100000)
            for df_chunk in tqdm(df_iter, desc=asset['name'], unit='chunk'):
                # convert string to datetime
                df_chunk.tpep_pickup_datetime = pd.to_datetime(df_chunk.tpep_pickup_datetime)
                df_chunk.tpep_dropoff_datetime = pd.to_datetime(df_chunk.tpep_dropoff_datetime)
                if first_chunk:  # create table only for the first chunk of the first asset
                    # TODO: new table name as parameter
                    df_chunk.head(0).to_sql(name='yellow_taxi_data', con=self.engine, if_exists='replace', index=False)
                    first_chunk = False
                df_chunk.to_sql(name='yellow_taxi_data', con=self.engine, if_exists='append', index=False)

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_DATABASE')
}

loader = YellowTaxiLoader(owner='DataTalksClub', 
                          repo='nyc-tlc-data', 
                          tag='yellow', 
                          db_config=db_config)
assets = loader.fetch_assets()
loader.load_assets(assets)