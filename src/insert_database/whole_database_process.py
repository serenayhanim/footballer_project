import os
import pandas as pd
import fnmatch
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from create_database_tables import create_tables
from insert_data_to_database import parse_time, insert_data
from calculate_sentiment import calculate_vader_sentiment, insert_data_to_vader_table
from update_footballer_table import update_footballers_table
from config import config

engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_test')
# engine = create_engine(f'postgresql://{config.USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_new')

# data_path = '/Users/serenay/Documents/HateLab/footballer_project/data/collection/footballer_data_c3/'
data_path = '/media/datalab1/Data1/serenay/footballer_project_db1/footballer_project/All_data/'
files = os.listdir(data_path)
print(files)

match_file = fnmatch.filter(files, '@*.csv')
print(match_file)

create_tables()

for file in match_file:
    path = data_path + file
    df = pd.read_csv(path, lineterminator="\n")
    insert_data(df, file)

analyzer = SentimentIntensityAnalyzer()
sentiment_df = pd.read_sql_query('select id, tweet from "tweets"', con=engine)

calculate_vader_sentiment(sentiment_df)
insert_data_to_vader_table(sentiment_df)
update_footballers_table()




