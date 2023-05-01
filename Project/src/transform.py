import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os.path

from params import conn_string, table_name, staging_data_dir
staging_file = "heart.parquet"

def transform():
    db = create_engine(conn_string)

    df = pd.read_sql_query(f'SELECT * FROM {table_name}',con=db)

    print(f"Shape of data {df.shape}")

    # write to parquet
    df.to_parquet(os.path.join(staging_data_dir, staging_file))

transform()