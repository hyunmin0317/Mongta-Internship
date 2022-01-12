import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.data.go.kr/data/15052860/fileData.do'
soup = BeautifulSoup(urlopen(url), 'html.parser')
d = []

for content in soup.find("div", class_='file-meta-table-pc').find_all("tr"):
    print(content.find('td').text)