import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data
import seaborn as sns 
from packages import * 

# first open file 
df = ''
df = open_file(df,'all_banks')


print('This is the data present in the file')

print(df)


print("Viewing returns of the period from 2006 to 2006 for Citi Bank, JP Morgan, Goldman Sachs, Wells Fargo and Morgan Stanley")

date_1 = '2006-01-01'
date_2 = '2016-12-31'

rate_of_return_over_a_period_with_plot(date_1,date_2,df)


max_min_std(date_1,date_2,df)

# displot_graph(date_1,date_2,df,'JPM')
# print('\n')
# displot_graph(date_1,date_2,df,'MS')
# print('\n')
# displot_graph(date_1,date_2,df,'GS')
# print('\n')
# displot_graph(date_1,date_2,df,'C')
# print('\n')
# displot_graph(date_1,date_2,df,'WFC')
# print('\n')