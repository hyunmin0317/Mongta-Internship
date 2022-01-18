import requests

def covid19_API():
    URL = 'http://localhost:9200/covid19_sample/_search?pretty'
    API = requests.get(URL).json()
    data = API['hits']['hits'][0]['_source']['TbCorona19CountStatus']['row']
    return data

if '__main__':
    data = covid19_API()

    for d in data:
        print(d['T_DT'])
        print(d)