import requests

def covid19_API():
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/5/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data

if '__main__':
    data = covid19_API()
    print(data)