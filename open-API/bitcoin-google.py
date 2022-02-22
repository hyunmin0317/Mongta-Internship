from pytrends.request import TrendReq
from datetime import datetime
import FinanceDataReader as fdr
from elasticsearch import Elasticsearch, helpers

def google_API():
    keywords = ["bitcoin"]
    pytrends = TrendReq(hl='ko', tz=360)

    pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='KR', gprop='')
    getdatainfo = pytrends.interest_over_time()

    list = []
    date_list = getdatainfo.index.to_list()
    value_list = getdatainfo['bitcoin'].to_list()

    for i in range(len(date_list)-1):
        dic = {"date":date_list[i].strftime("%Y-%m-%d"), "ratio":value_list[i]}
        list.append(dic)
    return list

def coin(name, date):
    df = fdr.DataReader(name, date)
    date_list = df.index.to_list()
    value_list = df['Close'].to_list()
    dic = {}

    for i in range(len(date_list)-1):
        dic[date_list[i].strftime("%Y-%m-%d")] = value_list[i]
    return dic

def coin_data(name, start):
    es = Elasticsearch(['http://3.34.219.4:9200/'])
    docs = []
    search_list = google_API()
    price_list = coin(name, start)

    for data in search_list:
        if data['date'] in price_list:
            date = data['date']
            doc = {
                "_index": "coin-google",
                "_id": name+date,
                "_source": {
                    "date": date,
                    "search": data['ratio'],
                    "price": price_list[date]
                }
            }
            docs.append(doc)
    print(docs)
    res = helpers.bulk(es, docs)

coin_data('BTC/KRW', '2020')