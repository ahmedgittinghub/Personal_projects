import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data
import seaborn as sns 





def open_file(variable,file_name):
    print("Opening file and retriving data")
    try:
        variable = pd.read_pickle(file_name)
    except FileNotFoundError as fnfe:
        print('file not found' + fnfe)
    finally:
        print("operation complete, data retrieved from the file correctly")

    return variable


def check_date(variable, checkdate):
    r = variable.split('-')
    checkdate = '0'

    print(r)
    
    if len(r) != 3: 
        print('invalid date inserted, date is not the correct length')
        checkdate = 'n'
        return checkdate

    elif len(r) == 3:
        print('date is the correct length, checking  if entry is valid')
        if r[0].isdigit() == False or r[1].isdigit() == False or r[2].isdigit() == False:
            print('date is inserted inncorrectly')
            checkdate = 'n'
            return checkdate
        
        elif r[0].isdigit() == True and r[1].isdigit() == True and r[2].isdigit() == True:
            if len(r[0]) != 4 or len(r[1]) != 2 or len(r[2]) != 2:
                print('date is inserted incorrectly')
                checkdate = 'n'
                return checkdate
            elif len(r[0]) == 4 and len(r[1]) == 2 and len(r[2]) == 2:
               print('date is inserted correctly')
               checkdate = 'y'
               return checkdate
    
    return checkdate


def rate_of_return_over_a_period_with_plot(date1,date2,dataframe):
    # create a new empty data frame
    returns_df = pd.DataFrame()
    # first iterate through the data frame:
    for stock_ticker in dataframe.columns.levels[0][1:]:
        close_prices = dataframe[stock_ticker]['Close']
        # calculating raturns
        returns_calculation = close_prices.pct_change()
         # workout the percentage change for the date period inserted
        returns = returns_calculation.loc[date1:date2]
        
        # adding the changes to the 
        returns_df[stock_ticker] = returns

        print(f"Final returns for {stock_ticker}: {returns.iloc[-1]}")
    


# This is a function that will allow you to view the max min and standard devation for each stock over a time period
def max_min_std(date1,date2,dataframe):
    returns_df = pd.DataFrame()
    for stock_ticker in dataframe.columns.levels[0][1:]:
        close_prices = dataframe[stock_ticker]['Close']
        # calculating raturns
        returns_calculation = close_prices.pct_change()
         # workout the percentage change for the date period inserted
        returns = returns_calculation.loc[date1:date2]
        returns_df[stock_ticker] = returns

    print('The minimum return for each stock is the following:')
    min_returns_dates = returns_df.idxmin()
    print(returns_df.loc[min_returns_dates, :])
    print('\n')

    print('The maximum return for each stock is The following:')
    max_returns_dates = returns_df.idxmax()
    print(returns_df.loc[max_returns_dates, :])
   

    print('\n')
    print('Now looking at the standard devation for each stock, The one with the highest standard devation value is the riskiest')
    print(returns_df.std())


# This function creates a graph for returns of each stock
def displot_graph(date1,date2,dataframe,bankname):
    returns_df = pd.DataFrame()
    for stock_ticker in dataframe.columns.levels[0][1:]:
        close_prices = dataframe[stock_ticker]['Close']
        # calculating raturns
        returns_calculation = close_prices.pct_change()
         # workout the percentage change for the date period inserted
        returns = returns_calculation.loc[date1:date2]
        returns_df[stock_ticker] = returns
    sns.displot(returns_df.loc[date1:date2][bankname],color='green',bins=100)
    

