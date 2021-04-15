select distinct on (fb.search) fb.search, tw.date as first_tweet_date                                         
from footballers fb
join screen_name_tweets snt ON snt.search = fb.search
join tweets tw on tw.id = snt.id
order by fb.search, tw.date;


select distinct on (fb.search) fb.search, tw.date as last_tweet_date                                         
from footballers fb
join screen_name_tweets snt ON snt.search = fb.search
join tweets tw on tw.id = snt.id
order by fb.search, tw.date desc;