import os
import pandas as pd
import fnmatch
from sqlalchemy import create_engine
from config import config

engine = create_engine(f'postgresql://{config.USERNAME}:{config.PASSWORD}@{config.IP_ADDRESS}/footballer_new')

data_path = '../data/collection/footballer_data_c3/'
files = os.listdir(data_path)

match_file = fnmatch.filter(files, '@*.csv')
print(match_file)


for file in match_file:
    df = pd.read_csv(file, lineterminator="\n")
    tweets_table = df[
        ["id", "conversation_id", "user_id", "created_at", "date", "timezone", "place", "tweet", "language", "hashtags",
         "cashtags", "day", "hour", "link", "urls", "photos", "video", "thumbnail", "retweet", "nlikes", "nreplies",
         "nretweets", "quote_url", "search", "reply_to"]]
    tweets_table.to_sql('tweets', con=engine, if_exists='append')
print("Tweets data is inserted to the tweets table")

# for file in match_file:
#     df = pd.read_csv(file, lineterminator="\n")
#     users_table = df[["user_id", "user_id_str", "username", "name"]]
#     users_table.drop_duplicates(subset = "user_id" , inplace =True)
#     users_table.to_sql('users', engine, if_exists='append')
# print("Users table is inserted to the database")
