import twint
import nest_asyncio
nest_asyncio.apply() 


def scrape_data(mention, since_date, until_date, csv_name):
    c = twint.Config()
    c.Search = mention
    c.Since = since_date
    c.Until = until_date
    c.Pandas = True
    twint.run.Search(c)
    Tweetsall_df = twint.storage.panda.Tweets_df
    Tweetsall_df.to_csv(csv_name + ".csv")
    return Tweetsall_df

# scrape_data(mention ='@sterling7', since_date = "2012-07-05", until_date = "2019-09-29", csv_name = 'sterling7')

    
