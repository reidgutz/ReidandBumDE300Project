from sqlalchemy import create_engine
import pandas as pd

from params import conn_string

def insert_to_table(data: pd.DataFrame, table_name:str):
    db = create_engine(conn_string)
    conn = db.connect()
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
