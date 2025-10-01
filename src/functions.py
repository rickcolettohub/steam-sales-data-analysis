import pandas as pd
import os


def load_all_csvs(raw_dir):
    dfs = {}
    for file in os.listdir(raw_dir):
        if file.endswith(".csv"):
            key = file.replace(".csv", "")
            dfs[key] = pd.read_csv(os.path.join(raw_dir, file))
            print(f"Loaded: {file} -> dataframes['{key}']")
    return dfs
