from sqlalchemy import create_engine
from config import config

# engine = create_engine(f'postgresql://{config.LOCAL_USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_test')
engine = create_engine(f'postgresql://{config.USERNAME}@{config.LOCAL_IP_ADDRESS}/footballer_new')


def create_tables():
    """Function creates all needed table in the database."""

    engine.execute('''
                                            DROP TABLE IF EXISTS users;
                                            CREATE TABLE users (
                                            user_id bigint PRIMARY KEY,
                                            user_id_str bigint,
                                            username text,
                                            name text)
                                            ''')

    engine.execute('''
                                                DROP TABLE IF EXISTS footballers;
                                                CREATE TABLE footballers (
                                                search text PRIMARY KEY,
                                                first_tweet_date date,
                                                last_tweet_date date,
                                                count integer
                                                 )
                                                ''')

    engine.execute('''
                                            DROP TABLE IF EXISTS tweets;
                                            CREATE TABLE tweets (
                                            id bigint NOT NULL PRIMARY KEY,
                                            conversation_id bigint,
                                            user_id bigint,
                                            created_at text,
                                            created_at_parsed timestamp,
                                            date date,
                                            timezone int,
                                            place float,
                                            tweet text,
                                            language text,
                                            hashtags text,
                                            day bigint,
                                            hour bigint,
                                            link text,
                                            urls text,
                                            photos text,
                                            video bigint,
                                            thumbnail float,
                                            retweet boolean,
                                            nlikes bigint,
                                            nreplies bigint,
                                            nretweets bigint,
                                            quote_url text,
                                            FOREIGN KEY (user_id)
                                                REFERENCES users (user_id)
    )''')

    engine.execute('''
                                        DROP TABLE IF EXISTS screen_name_tweets;
                                        CREATE TABLE screen_name_tweets (
                                        screen_name_tweets_id serial PRIMARY KEY ,
                                        id bigint NOT NULL ,
                                        reply_to text,
                                        search text NOT NULL,
                                        FOREIGN KEY (id)
                                        REFERENCES tweets (id),
                                        FOREIGN KEY (search)
                                        REFERENCES footballers (search))''')

    engine.execute('''
                                                DROP TABLE IF EXISTS vader_sentiments;
                                                CREATE TABLE vader_sentiments (
                                                sentiment_id serial PRIMARY KEY,
                                                id bigint NOT NULL ,
                                                positive decimal NOT NULL ,
                                                negative decimal NOT NULL ,
                                                compound decimal NOT NULL ,
                                                type text NOT NULL)''')
