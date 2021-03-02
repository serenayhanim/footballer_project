library(tidyverse)
library(rtweet)

# read datafrom disc
mentions_df <- read_csv("/Users/serenay/Documents/HateLab/league_players_start_end_dates.csv") %>%
  mutate(mentions2= str_remove(pattern = "@",string = mentions))

# lookup twitter api
mentions_metadata <- mentions_df %>% 
  select(mentions2) %>%
  map_df(lookup_users)

# process data from twitter 
account_date_info <- mentions_metadata %>% 
  mutate(screen_name2= tolower(screen_name)) %>% 
  select(screen_name2, account_created_at)

mentions_df_dates <- mentions_df %>% 
  left_join(account_date_info, by = c("mentions2" = "screen_name2") ) 

mentions_df_dates %>% 
  filter(account_created_at<first_date)

mentions_df_dates %>% 
  mutate(account_created_at_lead = account_created_at+lubridate::days(14)) %>% 
  filter(account_created_at_lead<first_date) %>% 
  mutate(date_diff = first_date - account_created_at)

