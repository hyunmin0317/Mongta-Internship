import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main(n):
    m=250
    BASIC = 'https://www.data.go.kr'

    try:
        for i in range(1,n+1):
            URL = BASIC+'/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=updtDt&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='+str(i)+'&perPage='+str(m)+'&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
            urls = []
            data = []

            soup = BeautifulSoup(urlopen(URL), 'html.parser')
            for href in soup.find("div", class_='result-list').find_all("dt"):
                urls.append(BASIC+href.find("a")["href"])

            # columns = []
            for url in urls:
                soup = BeautifulSoup(urlopen(url), 'html.parser')
                d = []

                for content in soup.find("div", class_='file-meta-table-pc').find_all("tr"):
                    td = (content.find('td').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
                    d.append(td)
                    # th = (content.find('th').text).replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
                    # columns.append(th)
                d.append(url)
                data.append(d)
                print(len(data))
    except:
        pass

    df = pd.DataFrame(data)
    print(df)
    df.to_csv('public-data.csv', index=False, encoding='cp949')

if __name__ == '__main__':
    main(2)