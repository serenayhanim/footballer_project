import fnmatch
import os
from sqlalchemy import create_engine
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import create_database_tables as ct
import insert_data_to_database as idd
import calculate_sentiment as cs
import update_footballer_table as uft
from config import config

engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}:{config.PASSWORD}@\
{config.LOCAL_IP_ADDRESS}/{config.DATABASE_NAME}')
analyzer = SentimentIntensityAnalyzer()


data_path = config.LOCAL_DATA_PATH
files = os.listdir(data_path)
match_file = fnmatch.filter(files, '@*.csv')

ct.create_tables(engine)
for iteration, file in enumerate(match_file[2:25]):
    print(f"********************** writing {iteration+1} of {len(match_file[2:25])} files **************************\n")
    path = data_path + file
    df = pd.read_csv(path, lineterminator="\n")
    idd.insert_data(df, file, engine)

sentiment_df = pd.read_sql_query('select id, tweet from "tweets"', con=engine)
cs.calculate_vader_sentiment(sentiment_df, analyzer)
cs.insert_data_to_vader_table(sentiment_df, engine)

uft.update_footballers_table(engine)
