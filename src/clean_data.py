import pandas as pd
import os
import functions as func

RAW_DIR = "data/raw"
dataframes = func.load_all_csvs(RAW_DIR)
