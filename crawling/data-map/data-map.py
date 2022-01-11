import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'http://www.bigdata-map.kr/search/'
url = 'http://www.bigdata-map.kr/search/2647572'
# data = []
soup = BeautifulSoup(urlopen(url), "html.parser")

# soup = BeautifulSoup(urlopen(url), 'html.parser')
print(soup)
# d = []
# for content in soup.find("ul", class_='board-view-new'):
#     print(content)
    # dd = (content.find('dd').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
    # d.append(dd)
    # th = (content.find('th').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
    # columns.append(th)
# data.append(d)
# print(data)

# df = pd.DataFrame(data)
# print(df)
# df.to_csv('data-map.csv', index=False, encoding='cp949')