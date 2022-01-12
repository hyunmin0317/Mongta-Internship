from urllib import request
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.data.go.kr/data/15052860/fileData.do'

source_code_from_URL = urllib.request.urlopen(URL)
soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

title=soup.find('meta', attrs = {'name':'title'})['content']
description=soup.find('meta', attrs = {'name':'description'})['content']
print(soup)
print(title)
