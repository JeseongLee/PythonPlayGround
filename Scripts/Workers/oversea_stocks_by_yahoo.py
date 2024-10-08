from bs4 import BeautifulSoup as bs
from datetime import datetime
from collections import defaultdict
import yfinance as yf
import requests
import pandas
import json
import urllib3
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get(isinCode):    
    print('get isinCode :: ' + isinCode)
    response = requests.get('https://query2.finance.yahoo.com/v1/finance/search', params={'q': isinCode}, verify=False, headers = {
        'User-agent': 'Mozilla/5.0',
        'Content-Type': 'application/json',
    })
    try:
        obj = response.json()
        print(obj['quotes'][0])
        return obj['quotes'][0]
    except:
        return {}

def getValue(obj, key):
    if key in obj:
        return obj[key]
    else:
        return ''
    
now = datetime.now()
isinCodeData = pandas.read_csv('C:/Users/11279/Downloads/isin_code.csv')
# print(isinCodeData['isin_code'])
print(isinCodeData['isin_code'].size)
isinCodeList = isinCodeData['isin_code']
dataFrame = {
    'isin': [],
    'exchange': [],
    'shortname': [],
    'quoteType': [],
    'symbol': [],
    'index': [],
    'score': [],
    'typeDisp': [],
    'longname': [],
    'exchDisp': [],
    'sector': [],
    'sectorDisp': [],
    'industry': [],
    'industryDisp': [],
    'isYahooFinance': [],
}
total = isinCodeList.size
count = 0
for isinCode in isinCodeList:
    count += 1
    print('PROGRESS :: ' + str(count) + '/' + str(total) + ' [' + str(round(count/total*100, 2)) + '%]')
    stock = get(isinCode)
    dataFrame['isin'].append(isinCode)
    dataFrame['exchange'].append(getValue(stock, 'exchange'))
    dataFrame['shortname'].append(getValue(stock, 'shortname'))
    dataFrame['quoteType'].append(getValue(stock, 'quoteType'))
    dataFrame['symbol'].append(getValue(stock, 'symbol'))
    dataFrame['index'].append(getValue(stock, 'index'))
    dataFrame['score'].append(getValue(stock, 'score'))
    dataFrame['typeDisp'].append(getValue(stock, 'typeDisp'))
    dataFrame['longname'].append(getValue(stock, 'longname'))
    dataFrame['exchDisp'].append(getValue(stock, 'exchDisp'))
    dataFrame['sector'].append(getValue(stock, 'sector'))
    dataFrame['sectorDisp'].append(getValue(stock, 'sectorDisp'))
    dataFrame['industry'].append(getValue(stock, 'industry'))
    dataFrame['industryDisp'].append(getValue(stock, 'industryDisp'))
    dataFrame['isYahooFinance'].append(getValue(stock, 'isYahooFinance'))
    # if count == 10: break

print(dataFrame)    
result = pandas.DataFrame(dataFrame)
print(result)
now = datetime.now()
result.to_csv('C:/Users/11279/Documents/isin-ticker/result_' + now.strftime('%Y%m%d%H%M%S') + '.csv', encoding='utf-8-sig')    