import pandas as pd
from sqlalchemy import create_engine
from config import config

engine = create_engine(f'postgresql://{config.USERNAME}:{config.PASSWORD}@{config.IP_ADDRESS}/footballer_new')

df = pd.read_sql_query('select * from "users"', con=engine)

print(df.head())

print('before drop')

print(df.shape[0])

# Drop duplicates from user table to create a primary key for user_id
df.drop_duplicates(subset="user_id", inplace=True)

print('after drop')
print(df.shape[0])

# Insert df to the user table
df.to_sql('users', con=engine, if_exists='replace')
