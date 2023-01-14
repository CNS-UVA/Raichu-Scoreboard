"""Docstring here so Pylint doesn't complain"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from scoreboard.models import Credential, TeamService


def index(request):
    """Index view? idk"""
    return render(request, 'index.html')


@login_required()
def credentials(request):
    """Shows user's team's submited credentials"""
    data = {
        'credentials': Credential.objects.filter(
            service__team=request.user.team
        )
    }
    return render(request, 'credentials.html', data)


@login_required()
def services(request):
    """Shows user's team's services"""
    data = {
        'services': TeamService.objects.filter(
            team=request.user.team
        )
    }
    return render(request, 'services.html', data)
