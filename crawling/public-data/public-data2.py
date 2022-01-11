import csv
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

urls = []
data = []
f = open("link.csv", 'r')
rea = csv.reader(f)
for row in rea:
    urls.append(str(row[0]))
f.close

for url in urls:
    print(url)
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    d = []
    for content in soup.find("div", class_='file-meta-table-pc').find_all("tr"):
        td = (content.find('td').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
        d.append(td)
        # th = (content.find('th').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
        # columns.append(th)
    data.append(d)

df = pd.DataFrame(data, index=urls)
print(df)
df.to_csv('public-data.csv', index=False, encoding='cp949')