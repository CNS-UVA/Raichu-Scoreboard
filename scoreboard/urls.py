"""Defines scoreboard URLs"""
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('credentials', views.credentials, name='credentials')
]
