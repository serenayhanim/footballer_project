
def create_tables(engine):
    """Function creates all needed table in the database.
    @type engine: object
    """

    engine.execute('''
                            
                                            CREATE TABLE users (
                                            user_id bigint PRIMARY KEY,
                                            user_id_str bigint,
                                            username text,
                                            name text)
                                            ''')

    engine.execute('''
                                               
                                                CREATE TABLE footballers (
                                                search text PRIMARY KEY,
                                                first_tweet_date date,
                                                last_tweet_date date,
                                                count integer
                                                 )
                                                ''')

    engine.execute('''
                                            
                                            CREATE TABLE tweets (
                                            id bigint NOT NULL PRIMARY KEY,
                                            conversation_id bigint,
                                            user_id bigint,
                                            created_at text,
                                            created_at_parsed timestamp,
                                            date date,
                                            timezone bigint,
                                            place text,
                                            tweet text,
                                            language text,
                                            hashtags text,
                                            cashtags text,
                                            day bigint,
                                            hour bigint,
                                            link text,
                                            urls text,
                                            photos text,
                                            video bigint,
                                            thumbnail text,
                                            retweet boolean,
                                            nlikes bigint,
                                            nreplies bigint,
                                            nretweets bigint,
                                            quote_url text,
                                            FOREIGN KEY (user_id)
                                                REFERENCES users (user_id)
    )''')

    engine.execute('''
                                        
                                        CREATE TABLE screen_name_tweets (
    									screen_name_tweets_id serial PRIMARY KEY,
                                        id bigint NOT NULL ,
                                        reply_to text,
                                        search text NOT NULL,
                                        FOREIGN KEY (id)
                                        REFERENCES tweets (id),
                                        FOREIGN KEY (search)
                                        REFERENCES footballers (search))''')

    engine.execute('''
                                                
                                                CREATE TABLE vader_sentiments (
                                                sentiment_id serial PRIMARY KEY,
                                                id bigint NOT NULL ,
                                                positive decimal NOT NULL ,
                                                negative decimal NOT NULL ,
                                                compound decimal NOT NULL ,
                                                type text NOT NULL)''')


