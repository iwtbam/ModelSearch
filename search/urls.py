# -*- coding:utf8 -*-

from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index,name="search"),
    path('results/', views.result, name="result"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),

]