import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main(n):
    BASIC = 'https://www.data.go.kr'
    URL = BASIC+'/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=updtDt&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage='+str(n)+'&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='

    urls = []
    data = []

    soup = BeautifulSoup(urlopen(URL), 'html.parser')
    for href in soup.find("div", class_='result-list').find_all("dt"):
        urls.append(BASIC+href.find("a")["href"])



    for url in urls:
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        d = []

        try:
            for content in soup.find("div", class_='file-meta-table-pc').find_all("tr"):
                td = (content.find('td').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
                d.append(td)

            if len(d) == 14:
                d.append(url)
            else:
                url = d[10]
                d[10:] = d[11:]
                d.append(url)
            data.append(d)
            print(len(data))
        except:
            pass

    df = pd.DataFrame(data)
    print(df)
    df.to_csv('DB.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main(1000)