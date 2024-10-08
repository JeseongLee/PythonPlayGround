from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import pandas
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get():
    try:
        return requests.get('http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201', verify=False, headers={'User-agent': 'Mozilla/5.0'})
    except:
        return None
    
response = get()
htmlText = response.text
# print(htmlText)
html = bs(htmlText, 'lxml')
evenList = html.find_all('tr', 'CI-GRID-EVEN')
print(evenList)
oddList = html.find_all('tr', 'CI-GRID-ODD')
print(oddList)