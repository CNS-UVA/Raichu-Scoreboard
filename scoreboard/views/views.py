"""Docstring here so Pylint doesn't complain"""
from django.db.models.functions import Concat
from django.shortcuts import render
from django.db.models import F, Value
from django.contrib.auth.decorators import login_required

from scoreboard.models import Service


def index(request):
    """Index view? idk"""
    return render(request, 'index.html')


@login_required()
def services(request):
    """Shows user's team's services and credentials"""
    services_data = Service.objects.all()  # Every team should have one of every service
    # scores = Score.objects.filter(team=request.user)

    # Note: we can't just use Credential objects because not every Service has a Credential
    # credentials = request.user.credential_set.all()

    services_data = services_data.annotate(
        ip=Concat(Value(f'{request.user.subnet}.'), F('ip_suffix')))

    # pylint: disable=invalid-name
    # Disabling so Pylint allows TheFunny
    TheContext = {
        'services': services_data,
        'team': request.user
    }
    return render(request, 'services.html', TheContext)
