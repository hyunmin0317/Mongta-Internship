from django.contrib import admin
from django.urls import path, include
from covid19 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('covid19/', include('covid19.urls')),
]
