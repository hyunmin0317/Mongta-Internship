from django.urls import path
from .views import detail

urlpatterns = [
    path('<int:n>/', detail, name='detail'),
]