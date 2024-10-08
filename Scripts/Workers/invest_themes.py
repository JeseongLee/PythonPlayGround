from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import pandas
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
def getHost():
    return 'https://finance.naver.com'
def getThemePath():
    return '/sise/theme.naver'
def getUrl(path):
    url = getHost()
    print('URL :: ' + url + path)
    return url + path
def get(path):
    try:
        return requests.get(getUrl(path), verify=False, headers={'User-agent': 'Mozilla/5.0'})
    except:
        return None
def getHtml(path):
    response = get(path)
    htmlText = response.text
    # print(htmlText)
    return bs(htmlText, 'lxml')
def getLastPage():
    themePath = getThemePath()
    html = getHtml(themePath)
    # print(html)
    tagPgRR = html.find('td', 'pgRR')
    print(tagPgRR)
    print(tagPgRR.a['href'])
    lastPageTags = tagPgRR.a['href'].split('=')
    print(lastPageTags)
    return lastPageTags[-1]
def getThemeList(lastPage):
    themeList = []
    for page in range(1, int(lastPage)+1):
        print(page)
        themePath = getThemePath()
        html = getHtml(themePath + '?&page=' + str(page))
        themeList += html.find_all('td', 'col_type1') # 테마담는다
    return themeList
def getProoductList(theme, themeDetailPath):
    detailHtml = getHtml(themeDetailPath)
    divList = detailHtml.find_all('div', 'name_area')
    themes = []
    names = []
    codes = []
    for row in divList:
        themes.append(theme)
        names.append(row.a.find_next(string=True).get_text(strip=True))
        codes.append(row.a['href'].split('=')[-1])
    return {
        'theme': themes,
        'name': names,
        'code': codes,
    }

lastPage = getLastPage()
print(lastPage)
themeList = getThemeList(lastPage)
print(themeList)
dataFrame = {
    'theme': [],
    'name': [],
    'code': [],
}
for row in themeList:
    themeName = row.a.find_next(string=True).get_text(strip=True)
    themeDetailPath = row.a['href']
    print(themeName + ' :: ' + themeDetailPath)
    themeDataFrame = getProoductList(themeName, themeDetailPath)
    dataFrame['theme'] += themeDataFrame['theme']
    dataFrame['name'] += themeDataFrame['name']
    dataFrame['code'] += themeDataFrame['code']
# print(dataFrame)
result = pandas.DataFrame(dataFrame)
print(result)
now = datetime.now()
result.to_excel('result_' + now.strftime('%Y%m%d%H%M%S') + '.xlsx')