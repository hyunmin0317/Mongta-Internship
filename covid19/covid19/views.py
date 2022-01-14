from django.shortcuts import render
import requests

def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data

def home(request):
    data = covid19_API(5)
    context = {'data': data}
    return render(request, 'home.html', context)

def detail(request, n):
    data = covid19_API(n)
    context = {'data': data}
    return render(request, 'home.html', context)