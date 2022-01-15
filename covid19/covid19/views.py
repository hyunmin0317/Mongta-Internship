from django.shortcuts import render
import requests

def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data

def home(request):
    today = covid19_API(1)[0]
    data_week = covid19_API(7)
    data_list = covid19_API(365)
    data_week.reverse()
    data_list.reverse()
    context = {"today":today, "data_week":data_week, "data_list":data_list}
    return render(request, 'home.html', context)