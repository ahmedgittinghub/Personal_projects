from packages1 import *
import bs4 as bs
import requests
import numpy as np
import pandas as pd
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data as wb

from datetime import datetime, timedelta

# setting start date and the end date 
current_date = datetime.now()
end_date = current_date - timedelta(days=1)
start_date = current_date - timedelta(days=7)

# Format the start date as a string
start_date_str = start_date.strftime("%Y-%m-%d")
current_date_str = current_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

tickers = []

tickers = ticker_extractor(tickers)

# downloading data from yahoo finance 

data = yf.download(tickers, start=start_date, end=current_date_str)

# deleting all failed data 
data = data.dropna(axis=1)

# seperating data so that its easy to interpret 
adj_close_df = data['Adj Close'].copy()
open_df = data['Open'].copy()
close_df = data['Close'].copy()
high_df = data['High'].copy()
low_df = data['Low'].copy()


#  Now creting a list of tickers that are available in the data frame
tickers = data['Adj Close'].columns.tolist()

# Now creating a list of dates for the dates available in the data frame
dates = close_df.index.tolist()

dates2 = []
for i in dates:
    dates2.append(str(i).replace('Timestamp','').replace('00:00:00','').replace(' ',''))

list_of_returns = []
list_of_returns = returns_calculator(tickers, dates2, close_df, open_df, list_of_returns)



print('\n')
print(f'The following analysis is for the s&p 500 stocks from  {dates2[0]} to {dates2[4]}')
# Creating a dataframe of the returns data 
returns_df = pd.DataFrame.from_dict(list_of_returns)

print('\n')
print("The following list of stocks is the ones with the best returns:")
# creating a data frame of the stocks with the best returns for the past week.
returns_df = returns_df.sort_values(by='stock_returns', ascending=False)

print(returns_df.head(5))

print('\n')
print("The following list of stocks generated the worst losses:")

print(returns_df.tail(5))


volatility_of_each_stock = []

volatility_of_each_stock = stock_volatility_calculator(volatility_of_each_stock, dates2, tickers, close_df, open_df)


#  creating a datafram for the volatility


volatility_df = pd.DataFrame.from_dict(volatility_of_each_stock)

# volatility_df
print('\n')
print("The following list of stocks is the most volatile stocks:")

volatility_df = volatility_df.sort_values(by='Stock_Volatility', ascending=False)


print(volatility_df.head(5))

print('\n')
print('\n')
print('\n')                                     