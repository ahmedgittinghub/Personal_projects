# List of packages that will be used 

# this function will be used to extract ticker name from  the internet  
def ticker_extractor(list_name):
    
    import bs4 as bs
    import requests
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        list_name.append(ticker.replace('\n', ''))
        
    

    return list_name


# This function will be used to calculate the returns of each stock
def returns_calculator(list_of_tickers, list_of_dates, close_data_frame, open_data_frame, new_list):
    dict_1 = {'ticker_name': '' , 'stock_returns' : '', 'stock_%returns': '' }

    start_date = list_of_dates[0]
    
    end_date = list_of_dates[4]



    for ticker in list_of_tickers:
        dict_1['ticker_name'] = ticker
        # calculating  & rounding up returns 
        dict_1['stock_returns'] = (close_data_frame.loc[end_date, ticker] - open_data_frame.loc[start_date, ticker]).round(2)
        # Converting to a string
        dict_1['stock_returns'] = '$' + str(dict_1['stock_returns'])

        # calculating percentage returns 
        dict_1['stock_%returns'] = ((close_data_frame.loc[end_date, ticker] - open_data_frame.loc[start_date, ticker]) * 100/(open_data_frame.loc[start_date,ticker])).round(2)
        dict_1['stock_%returns'] = '%' + str(dict_1['stock_%returns'])
        new_list.append(dict_1)
        dict_1 = {'ticker_name': '' , 'stock_returns' : '', 'stock_%returns': '' }
    
    return new_list


# This function will be used to calculate the Volatility of each stock 
def stock_volatility_calculator(new_list, list_of_dates, list_of_tickers, close_data, open_data,):
    
    day_1 = list_of_dates[0]
    day_2 = list_of_dates[1]
    day_3 = list_of_dates[2]
    day_4 = list_of_dates[3]
    day_5 = list_of_dates[4]

    dict_2 = {'Stock_Ticker':'', 'Stock_Volatility':''}

    for ticker in list_of_tickers:
        day_1_returns = ((close_data.loc[day_1, ticker] - open_data.loc[day_1, ticker]) * 100/(open_data.loc[day_1,ticker]))
        day_2_returns = ((close_data.loc[day_2, ticker] - open_data.loc[day_2, ticker]) * 100/(open_data.loc[day_2,ticker]))
        day_3_returns = ((close_data.loc[day_3, ticker] - open_data.loc[day_3, ticker]) * 100/(open_data.loc[day_3,ticker]))
        day_4_returns = ((close_data.loc[day_4, ticker] - open_data.loc[day_4, ticker]) * 100/(open_data.loc[day_4,ticker]))
        day_5_returns = ((close_data.loc[day_5, ticker] - open_data.loc[day_5, ticker]) * 100/(open_data.loc[day_5,ticker]))

        mean_return = (day_1_returns + day_2_returns + day_3_returns + day_4_returns + day_5_returns) / 5

        variance = ((day_1_returns - mean_return)**2 + (day_2_returns - mean_return)**2 + (day_3_returns - mean_return)**2 + (day_4_returns - mean_return)**2 + (day_5_returns - mean_return)**2) / 4

        standard_deviation = (variance**0.5).round(2)

        dict_2['Stock_Ticker'] = ticker

        dict_2['Stock_Volatility'] = standard_deviation

        new_list.append(dict_2)

        dict_2 = {'Stock_Ticker':'', 'Stock_Volatility':''}
    
    return new_list