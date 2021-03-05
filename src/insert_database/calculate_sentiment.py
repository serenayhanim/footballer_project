from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import config

engine = create_engine(f'postgresql://{config.USERNAME}:{config.PASSWORD}@{config.IP_ADDRESS}/footballer_new')
# engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_test')
analyzer = SentimentIntensityAnalyzer()

# get all tweets from tweets table.
sentiment_df = pd.read_sql_query('select id, tweet from "tweets"', con=engine)


def calculate_vader_sentiment(dataframe):
    """
    Calculates sentiment scores of tweets and add a column for
    each score types (compound, positive, negative). Determines type of tweet sentimentally based on compound score.

    @param dataframe: dataframe
    """

    dataframe['compound'] = [analyzer.polarity_scores(x)['compound'] for x in zip(dataframe['tweet'])]
    dataframe['positive'] = [analyzer.polarity_scores(x)['pos'] for x in zip(dataframe['tweet'])]
    dataframe['negative'] = [analyzer.polarity_scores(x)['neg'] for x in zip(dataframe['tweet'])]
    print(f"Vader columns are generated for'{dataframe}'!")

    dataframe['type'] = np.where(dataframe['compound'] > 0.05, 'positive',
                                 (np.where(dataframe['compound'] < -0.05, 'negative', 'neutral')))
    print(f"Type column is generated for'{dataframe}'!")


def insert_data_to_vader_table(dataframe):
    """
    Create sentiment table dataframe from selecting id, positive, negative, compound and type columns.
    Insert the dataframe to the vader_sentiments table.

    @param dataframe: dataframe
    """

    sentiments_table = dataframe[["id", "positive", "negative", "compound", "type"]]
    sentiments_table.to_sql('vader_sentiments', engine, if_exists='append', index=False, chunksize=100)

