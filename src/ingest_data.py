import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Api kaggle
api = KaggleApi()
api.authenticate()

# Raw data Directory
RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# data set path
DATASET = "nikdavis/steam-store-games"

# download and unzip data
try:
    api.dataset_download_files(DATASET, path=RAW_DATA_DIR, unzip=True)
    print(f"Download Finished! Data saved on: {RAW_DATA_DIR}")
except Exception as e:
    print(f"Donload Error: {e}")
