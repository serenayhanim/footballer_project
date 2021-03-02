from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import config

# calculate sentiment scores of tweets in remote database
engine = create_engine(f'postgresql://{config.USERNAME}:{config.PASSWORD}@{config.IP_ADDRESS}/footballer_new')
analyzer = SentimentIntensityAnalyzer()
sentiment_df = pd.read_sql_query('select id, tweet from "tweets"', con=engine)


def sentiment(dataframe):
    dataframe['compound'] = [analyzer.polarity_scores(x)['compound'] for x in zip(dataframe['tweet'])]
    dataframe['pos'] = [analyzer.polarity_scores(x)['pos'] for x in zip(dataframe['tweet'])]
    dataframe['neg'] = [analyzer.polarity_scores(x)['neg'] for x in zip(dataframe['tweet'])]
    print(f"Vader columns are generated for'{dataframe}'!")

    dataframe['type'] = np.where(dataframe['compound'] > 0.05, 'positive',
                                 (np.where(dataframe['compound'] < -0.05, 'negative', 'neutral')))
    print(f"Type column is generated for'{dataframe}'!")


sentiment(sentiment_df)

sentiment_table = sentiment_df[["id", "pos", "neg", "compound", "type"]]
results = engine.execute('DROP TABLE IF EXISTS sentiments;')
sentiment_table.to_sql('sentiments', engine, if_exists='append')

# To create sentiment table
# sentiment_table = dataframe[["id", "pos", "neg", "compound", "type"]]
