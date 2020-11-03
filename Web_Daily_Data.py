"""
Created on Sat Jan 11 15:29:04 2020

"""
#!/usr/bin/env python3


def Web_Daily_Data(Ticker = [], Start ='' ,End ='',Choice ='' ,Source = 'yahoo'):
    """ Import Data from Quandl for choice 'Q' or Yahoo for Choice 'D'"""

    import datetime as dt

    Ticker = Ticker or input("Enter Tcikers separated by',': ").split(',')
    Choice = Choice or input(" Q for Quandl, D for Pandas-Data: ")
    Start = Start or input("Enter Start Date separated by '-':  ") or (dt.date.today()-
                           dt.timedelta(1825)).strftime('%Y-%m-%d')
    End = End or input("Enter Start Date separated by '-':  ") or (dt.date.today()).strftime('%Y-%m-%d')

    import pandas as pd
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.width', 1000)

    if Choice == 'Q':

        import quandl
        key_path = '/home/tinky/Python/Data/quandl_key.txt'
        quandl.ApiConfig.api_key = open(key_path,'r',encoding='utf-8-sig').read().strip()
        # get the table for daily stock prices and,
        # filter the table for selected tickers, columns within a time range
        # set paginate to True because Quandl limits tables API to 10,000 rows per call
        data = pd.DataFrame()
        for i in range(len(Ticker)):
            try:
                dat = quandl.get_table('WIKI/PRICES', ticker = Ticker[i],
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
                        date = { 'gte': Start, 'lte': End },
                        paginate=True)
                data[Ticker[i]] = dat.pivot(index='date',columns='ticker',values='adj_close')[Ticker[i]]
            except:
                print(f"Unable to get the Data for: {Ticker[i]}")
                continue

    else:

        import pandas_datareader.data as wb
        start = dt.datetime.strptime(Start, "%Y-%m-%d")
        end = dt.datetime.strptime(End, "%Y-%m-%d")
        data = pd.DataFrame()
        for i in range(len(Ticker)):
            try:
                data[Ticker[i]] = wb.DataReader(Ticker[i],Source, start, end)['Adj Close']
            except:
                 print(f"Unable to get the Data for: {Ticker[i]}")
                 continue

    return data














