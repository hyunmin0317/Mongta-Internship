from django.urls import path
from .views import home

app_name ='covid19'

urlpatterns = [
    path('', home, name='home'),
]