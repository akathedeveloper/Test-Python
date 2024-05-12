from django.contrib import admin
from django.urls import path
from home import views         #import views from home

urlpatterns = [
    path("", views.index, name="home"),            #if the path is empty, it will redirect to views.index function
]
