"""Docstring here so Pylint doesn't complain"""
from django.shortcuts import render

from scoreboard.models import *

# Create your views here.
def index(request):
    return render(request, 'scoreboard/index.html')

# TODO: redirect if not logged in
def credentials(request):
    # request.user.
    data = {
        'credentials': Credential.objects.filter(
            service__team=request.user.team
        )
    }
    print(len(data['credentials']))
    return render(request, 'scoreboard/credentials.html', data)
