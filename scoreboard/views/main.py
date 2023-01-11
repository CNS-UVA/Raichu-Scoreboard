"""Docstring here so Pylint doesn't complain"""
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'scoreboard/index.html')
