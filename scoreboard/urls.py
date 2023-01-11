"""Defines scoreboard URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('credentials', views.credentials, name='credentials'),
    path('services', views.services, name='services'),
    path('mickey', views.mickey, name='mickey')
]
