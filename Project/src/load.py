import glob
import os.path
import pandas as pd

from utilities import insert_to_table

from params import staging_data_dir
table_name = "heart_data"

"""
read parquet files in the staging folder and load to database
"""

def load() -> pd.DataFrame:
    data = pd.DataFrame()
    for parquet_file in glob.glob(os.path.join(staging_data_dir, "*.parquet")):
        data = pd.concat([pd.read_parquet(parquet_file),data])

    insert_to_table(data, table_name)

    return data

data = load()
print(data.shape)
