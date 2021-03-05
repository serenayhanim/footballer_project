import pandas as pd
from pangres import upsert


def update_footballers_table(engine):
    """
    Calculate start date, end date and tweet counts for each footballer(search).
    Create new columns for each of them and insert them to the footballers table in the database.
    @type engine: object
    """
    start_end_date_df = pd.read_sql_query(
        '''select *
                    from (
                    select distinct on (fb.search) fb.search, tw.date as first_tweet_date
                    from footballers fb
                    join screen_name_tweets snt ON snt.search = fb.search
                    join tweets tw on tw.id = snt.id
                    order by fb.search, tw.date
                    )f
                    join(
                    select distinct on (fb.search) fb.search, tw.date as last_tweet_date
                    from footballers fb
                    join screen_name_tweets snt ON snt.search = fb.search
                    join tweets tw on tw.id = snt.id
                    order by fb.search, tw.date desc
                    )l USING (search)''', con=engine)

    count_tweets_df = pd.read_sql_query(
        '''select count(search), search
                                    from screen_name_tweets
                                    group by search
                                    order by count(search) desc''', con=engine)

    footballers_complete_table = pd.merge(start_end_date_df, count_tweets_df, on="search")
    footballers_complete_table.set_index('search', inplace=True)
    # update data if the row(on the primary key column) that is being inserted already exists in the table.
    upsert(engine=engine,
           df=footballers_complete_table,
           table_name='footballers',
           if_row_exists='update')


