import datetime as dt
import pandas as pd
stockdata = input('Select the any one Company Name in yahoo finance\n')
ts1 = str(int(dt.datetime(2023,2,1).timestamp()))
ts2 = str(int(dt.datetime(2023,2,8).timestamp()))
interval = input('Enter the interval from 1d to 1mo :\n\t daywise = 1d\n\t weekwise = 1wk\n\t monthwise = 1mo\n')
events = input('Do you want me to print history or div data ? \n')
Stockurl = 'https://finance.yahoo.com/quote/'+stockdata+'/history?p='+stockdata+''
Stock_downurl = 'https://query1.finance.yahoo.com/v7/finance/download/' + stockdata + '?period1='+ ts1 + '&period2=' + ts2 + '&interval=' + interval + '&events'+ events
company_data = pd.read_csv(Stock_downurl)
print(company_data)
