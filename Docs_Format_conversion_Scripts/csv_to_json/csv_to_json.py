import pandas as pd
import os
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("--csv-path", required=True, help="Path to csv file")
args = vars(arg.parse_args())

# checking if file exists
csv_path = args["csv_path"]
if os.path.exists(csv_path):
    basename = os.path.basename(csv_path)
    json_file_name = os.path.splitext(basename)[0] + ".json"
    if basename.endswith(".csv"):
        data = pd.read_csv(csv_path)
        
        data.to_json(json_file_name, orient='records')
        del data
