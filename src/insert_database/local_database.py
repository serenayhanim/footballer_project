from sqlalchemy import create_engine
from config import config
import pandas as pd

# create engine instance
engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}@localhost/footballer')

# connect server
conn = engine.connect()

# to write pandas dataframe to a PostgreSQL table
tablename_df.to_sql('tablename', engine)

# to read from a PostgreSQL table to a pandas dataframe
dataframe = pd.read_sql("Query", conn)
