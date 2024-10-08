from bs4 import BeautifulSoup as bs
from datetime import datetime
from tiingo import TiingoClient
from collections import defaultdict
import requests
import pandas
import json
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def isAvailableExchange(param):
    containExchanges=['AMEX', 'NASDAQ', 'NYSE']
    for ex in containExchanges:
        if param in ex:
            return True
    return False

token = '1b563d62c367343222ac9c526249355d195d8fd6'
config = {}
config['session'] = True
config['api_key'] = token
client = TiingoClient(config)


def get():
    try:
        return requests.get('https://api.tiingo.com/tiingo/fundamentals/meta?token=' + token, verify=False, headers={'User-agent': 'Mozilla/5.0', 'Content-Type': 'application/json'})
    except:
        return None
    
now = datetime.now()

# print(json)
# print(client.list_tickers())
# tickers = client.list_stock_tickers()
# total = len(tickers)
# print('total :: ' + str(total))
# dataFrame = {
#     'exchange': [],
#     'ticker': []
# }

# for row in tickers:
#     if isAvailableExchange(row["exchange"]):
#         dataFrame['exchange'].append(row["exchange"])
#         dataFrame['ticker'].append(row["ticker"])
#         tickerMetadata = client.get_ticker_metadata(row["ticker"])
#         client.get_ticker_metadata
#         print(tickerMetadata)
        
# exchanges = pandas.DataFrame(dataFrame)
# exchanges.to_excel('oversea_tickers_ex_' + now.strftime('%Y%m%d%H%M%S') + '.xlsx')
    
#'ticker': '000488', 'exchange': 'SHE', 'assetType': 'Stock', 'priceCurrency': 'CNY', 'startDate': '2007-01-04', 'endDate': '2024-08-29'

response = get()
list = response.json()
total = len(list)
print('total :: ' + str(total))
dataFrame = {
    'isin': [],
    'ticker': [],
    'name': []
}
processPercent = 0
for i in range(total):
    processPercent = round((i+1)/total*100, 4)
    print(str(processPercent) + '% :: ' + str(i+1) + '/' + str(total))
    row = list[i]
    print(row)
    if row['isActive']:
        dataFrame['isin'].append(row["permaTicker"])
        dataFrame['ticker'].append(row["ticker"])
        dataFrame['name'].append(row["name"])
result = pandas.DataFrame(dataFrame)
result.to_excel('oversea_tickers_' + now.strftime('%Y%m%d%H%M%S') + '.xlsx')