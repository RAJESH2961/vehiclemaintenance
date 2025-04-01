from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),#Here name "home" is used in url links in pages


    
]



