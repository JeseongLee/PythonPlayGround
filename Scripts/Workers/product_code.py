import pandas as pd
df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', encoding='cp949')[0]
print(df.head())
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
df.sort_values(by='종목코드')
print(df.head())