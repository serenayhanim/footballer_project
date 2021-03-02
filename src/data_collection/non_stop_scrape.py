import twint
import pandas as pd
import nest_asyncio
import datetime
import time
import os
import fnmatch

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
    print(f"Collection with query: '{mention}' is complete!")
    return Tweetsall_df


accounts = pd.read_csv("accounts.csv")
twitter_accounts = accounts.username.tolist()
names = [str('@' + twitter_account) for twitter_account in twitter_accounts]
files = os.listdir('/Users/serenay/Desktop/logic_test')
match_file = fnmatch.filter(files, '@*.csv')
match_file_no_ext = [".".join(f.split(".")[:-1]) for f in match_file]
remain_names = list(set(names) - set(match_file_no_ext))
sleep_seconds = 3600

while len(remain_names) > 0:
    try:
        for name in remain_names:
            print(f"now scraping {name}==========================")
            print(f"time now is {datetime.datetime.now()}==========================")
            scrape_data(mention=name,
                        since_date="2020-10-01",
                        until_date="2020-10-05",
                        csv_name=name)
    except:
        time.sleep(sleep_seconds)
        print(f"sleeping for {sleep_seconds} seconds!============================")
        pass
    files = os.listdir('/Users/serenay/Desktop/logic_test')
    match_file = fnmatch.filter(files, '@*.csv')
    match_file_no_ext = [".".join(f.split(".")[:-1]) for f in match_file]
    remain_names = list(set(names) - set(match_file_no_ext))
