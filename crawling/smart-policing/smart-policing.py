import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

def crawling(n):
    BASIC = "https://www.bigdata-policing.kr/"
    data = []
    for i in range(1,n+1):
        URL = BASIC+'product/list?page='+str(n)+'&perPageNum=12&sort_id=idx&orderby=hit#review_content'
        urls = []
        soup = BeautifulSoup(urlopen(URL), 'html.parser')
        for href in soup.find_all("div", class_='box-card-wrap'):
            urls.append(BASIC + href.find("a")["href"])

        for url in urls:
            d = []
            soup = BeautifulSoup(urlopen(url), 'html.parser')

            d.append(soup.find("div", class_="tit").text)
            caption = soup.find("div", class_="caption")
            d.append(caption.select_one("em").text)
            date = soup.find("div", class_="date").text.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'').replace(u'\r', u'').split('/')
            d.append(date[0])
            d.append(date[1])

            for content in soup.find("ul", class_='list-info').find_all("dd"):
                d.append(content.text.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'').replace(u'\r', u''))
            d.append(url)
            data.append(d)
        print("epoch: "+str(i))

    df = pd.DataFrame(data)
    print(df)
    df.to_csv('smart-policing.csv', index=False, encoding='cp949')

if __name__ == '__main__':
    crawling(25)
