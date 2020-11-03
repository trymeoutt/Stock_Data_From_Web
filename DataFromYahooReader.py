#!/usr/bin/env python3
"""
Load Data from Yahoo reader
"""
# Load Data from web 

def load_financial_data(symbols, start_date,end_date,output_file):
    import pandas as pd
    from pandas_datareader import data

    try:
        df = pd.read_pickle(output_file)
        print('File data found...reading symbols data')
    except FileNotFoundError:
        print('File not found...downloading the symbols data')
        df = data.DataReader(symbols, 'yahoo', start_date,end_date)
        df.to_pickle(output_file)
    return df

import time 

symbolsIds = ['SPY','AAPL','ADBE','LUV','MSFT','SKYW','QCOM','HPQ','JNPR','AMD','IBM']
End = time.strftime('%Y-%m-%d')
Start =  str(int(End[:4]) - 20) + End[4:]


data_=load_financial_data(symbolsIds,start_date=Start,end_date = End,
                          output_file='multi_data_large.pkl')

data_['Adj Close']  # if you want adjclose you can use this 
data_['Close']  # if you want close you can use this 


