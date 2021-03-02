import random
import pandas as pd

dataframe = pd.read_csv('filename.csv')

# To create date and time column together
dataframe['datetime'] = dataframe['date'].astype(str) + " " + dataframe['time'].astype(str)

# To convert to datetime object
dataframe['datetime'] = pd.to_datetime(dataframe['datetime'], format='%Y-%m-%d %H:%M:%S')


def query_data(startdatetime, enddatetime, dataframe, columnname):
    '''startdatetime and enddatetime's format should be %Y-%m-%d %H:%M:%S '''

    data = dataframe[(dataframe['columnname'] >= 'startdatetime') & (dataframe['columnname'] <= 'enddatetime')]
    return data


# to generate a sample of data
# n = number of sample 
data_sample = dataframe.sample(n, random_state=111)
