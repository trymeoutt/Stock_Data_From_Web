#!/usr/bin/env python3
"""
Created on Fri Oct 30 13:57:20 2020

@author: Trymeoutt
"""

def YahooFinancials_Data_toFile(Ticker=[],Start='',End ='',Frequency ='daily'):
     
    """
    from yahoofinancials import YahooFinancials

    # Tickers
    tech_stocks = ['AAPL', 'MSFT', 'INTC']
    bank_stocks = ['WFC', 'BAC', 'C']
    commodity_futures = ['GC=F', 'SI=F', 'CL=F']
    cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
    currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
    mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
    us_treasuries = ['^TNX', '^IRX', '^TYX']

    # Classes for Obtaining Data 
    yahoo_financials_tech = YahooFinancials(tech_stocks)
    yahoo_financials_banks = YahooFinancials(bank_stocks)
    yahoo_financials_commodities = YahooFinancials(commodity_futures)
    yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
    yahoo_financials_currencies = YahooFinancials(currencies)
    yahoo_financials_mutualfunds = YahooFinancials(mutual_funds)
    yahoo_financials_treasuries = YahooFinancials(us_treasuries)

    # Financial Statements
    tech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('annual', 'cash')
    bank_cash_flow_data_an = yahoo_financials_banks.get_financial_stmts('annual', 'cash')
    banks_net_ebit = yahoo_financials_banks.get_ebit()

    # Data 
    tech_stock_price_data = yahoo_financials_tech.get_stock_price_data()
    daily_bank_stock_prices = yahoo_financials_banks.get_historical_price_data('2008-09-15','2018-09-15', 'daily')
    daily_commodity_prices = yahoo_financials_commodities.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
    daily_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
    daily_currency_prices = yahoo_financials_currencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
    daily_mutualfund_prices = yahoo_financials_mutualfunds.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
    daily_treasury_prices = yahoo_financials_treasuries.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
    """

    import pandas as pd
    from yahoofinancials import YahooFinancials
    import datetime as dt 
    import os
    source = '/home/****/Python/Code/Final'
    data_folder = os.path.join(source, 'Data')
#code_folder = os.path.join(source, 'Code/WebData')
##file_to_open = os.path.join(data_folder, "raw_data.txt")
##f = open(file_to_open)
    
    Ticker = Ticker or input("Enter Tcikers separated by',': ").split(',')
    Start = Start or input("Enter Start Date separated by '-':  ") or (dt.date.today()-
                           dt.timedelta(1825)).strftime("%Y-%m-%d")
    End = End or input("Enter End Date separated by '-':  ") or (dt.date.today()).strftime("%Y-%m-%d")
    Frequency = Frequency or input("Enter Frequency like 'daily','weekly':  ") or 'daily'
    
#    data = pd.DataFrame()
    if not os.path.exists(os.path.join(data_folder, 'stock_dfs')):
        os.makedirs(os.path.join(data_folder, 'stock_dfs'))
    for i in range(len(Ticker)):
        try:
            yahoo_financials = YahooFinancials(Ticker[i])
            Json_obj = yahoo_financials.get_historical_price_data(Start, End, Frequency)
            Ohlv = Json_obj[Ticker[i]]['prices']
#            temp = pd.DataFrame(Ohlv)[["formatted_date","adjclose"]]
            temp = pd.DataFrame(Ohlv)
            temp.set_index("formatted_date", inplace = True)
            temp = temp[~temp.index.duplicated(keep = 'first')]
            temp.to_csv(os.path.join(data_folder, 'stock_dfs/{}.csv').format(Ticker[i]))

#            data[Ticker[i]] = temp['adjclose']
        
        except:
            print(f"Unable to get the Data for: {Ticker[i]}")
            continue
    
import time
End = time.strftime('%Y-%m-%d')
Start =  str(int(End[:4]) - 20) + End[4:]
Ticker = ['AAPL', 'MSFT']
Frequency = 'daily'

YahooFinancials_Data_toFile(Ticker,Start,End,Frequency ='daily')
