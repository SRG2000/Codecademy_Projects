# Import relevant modules
import codecademylib3_seaborn
import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb
import numpy as np
from datetime import datetime 

# Load gold_prices and crude_oil_prices csv files
gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)
# Start and End dates for analysis (year, month, day)
start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)
# Load NASDAQ100 data from FRED API between start and end dates
nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
print(nasdaq_data)
# Load SP500 data from FRED API between start and end dates
sap_data = web.DataReader('SP500', 'fred', start, end)
print(sap_data)
# Load GDP data from World Bank API between start and end dates
gdp_data = wb.download(indicator = 'NY.GDP.MKTP.CD', country = ['US'], start = start, end = end)
print(gdp_data)
# Load Export data from World Bank API between start and end dates
export_data = wb.download(indicator = 'NE.EXP.GNFS.CN', country = ['US'], start = start, end = end)
print(export_data)

# Calculating log return
# Define log return function
def log_return(prices):
  return np.log(prices / prices.shift(1))
# Gold returns
gold_returns = log_return(gold_prices['Gold_Price'])
# Oil returns
crudeoil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
# SP500 returns
sap_returns = log_return(sap_data['SP500'])
# NASDAQ returns
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
# GDP growth
gdp_growth = log_return(gdp_data['NY.GDP.MKTP.CD'])
# Export growth
export_growth = log_return(export_data['NE.EXP.GNFS.CN'])

# Comparing return/growth volatility
# Gold
print('Gold:', gold_returns.var())
# Oil
print('Oil:', crudeoil_returns.var())
# SP500
print('SP500:', sap_returns.var())
# NASDAQ
print('NASDAQ:', nasdaq_returns.var())
# GDP 
print('GDP:', gdp_growth.var())
# Exports
print('Exports:', export_growth.var())
