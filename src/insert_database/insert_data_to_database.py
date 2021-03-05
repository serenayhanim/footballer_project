import datetime
import os
import pandas as pd
import fnmatch
from sqlalchemy import create_engine
from pangres import upsert
from config import config

# engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_test')


engine = create_engine(f'postgresql://{config.USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_new')


def parse_time(time_int: int) -> str:
    """
    converts integer timestamp into date

    @param time_int: int
    @return: str
    """

    time_stamp = datetime.datetime.fromtimestamp(time_int / 1000)
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    return time_stamp


def insert_data(dataframe, csv_file):
    """
    insert related data to the database tables.

    @param dataframe: dataframe
    @param csv_file: csv file
    """

    users_table = dataframe[["user_id", "user_id_str", "username", "name"]]
    print(f"---------------{csv_file}users table is created---------")
    users_table.drop_duplicates(subset="user_id", inplace=True)
    users_table.set_index('user_id', inplace=True)
    upsert(engine=engine,
           df=users_table,
           table_name='users',
           if_row_exists='update')
    print(f" {csv_file} Users table is inserted to the database")

    # Tweets table
    tweets_table = dataframe[
        ["id", "conversation_id", "user_id", "created_at", "date", "timezone", "place", "tweet", "language", "hashtags",
         "cashtags", "day", "hour", "link", "urls", "photos", "video", "thumbnail", "retweet", "nlikes", "nreplies",
         "nretweets", "quote_url"]]
    tweets_table["created_at_parsed"] = tweets_table["created_at"].apply(parse_time)
    print(f"---------------{csv_file} tweets table printed---------")
    tweets_table.drop_duplicates(subset=['id'], inplace=True, ignore_index=True)
    tweets_table.set_index('id', inplace=True)
    upsert(engine=engine,
           df=tweets_table,
           table_name='tweets',
           if_row_exists='update')
    print(f"---------------{csv_file} table was written in the database---------")

    # footballers table
    footballers_table = dataframe[['search']]
    footballers_table.drop_duplicates(subset=['search'], inplace=True, ignore_index=True)
    footballers_table.set_index('search', inplace=True)
    upsert(engine=engine,
           df=footballers_table,
           table_name='footballers',
           if_row_exists='update')
    print(f" {csv_file} Footballers table is inserted to the database")

    # screen_name_tweets table
    screen_name_tweets_table = dataframe[["id", "reply_to", "search"]]
    print(f"---------------{csv_file} screen_name_tweets table is created---------")
    screen_name_tweets_table.to_sql('screen_name_tweets', engine, if_exists='append', index=False, chunksize=100)
    print(f" {csv_file} Screen_name_tweets table is inserted to the database")


# List all files in the given path
data_path = '/media/datalab1/Data1/serenay/footballer_project_db1/footballer_project/All_data/'
files = os.listdir(data_path)
print(files)

# list all csv files in files
match_file = fnmatch.filter(files, '@*.csv')
print(match_file)

# create pandas dataframe for each csv file in the list and insert the data related table in the database.
for file in match_file[2:4]:
    path = data_path + file
    df = pd.read_csv(path, lineterminator="\n")
    insert_data(df, file)
