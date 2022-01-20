import requests

def subway_API(query):
    URL = 'http://localhost:9200/seoul_subway/_search?size=1000&q='+query
    data = requests.get(URL).json()['hits']['hits']
    return data

if '__main__':
    data = subway_API("01호선")

    if len(data) == 0:
        print("검색 결과가 없음")
    else:
        for d in data:
            station = d['_source']
            print(station['line']+" "+station['station']+" "+station['number'])