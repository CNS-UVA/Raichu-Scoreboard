"""Docstring here so Pylint doesn't complain"""
from django.contrib.auth import authenticate, login
from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.db.models import F, Value
from django.contrib.auth.decorators import login_required

from scoreboard.models import Service


async def index(request):
    """Index view? idk"""
    from scoreboard.consumers import DashboardConsumer
    from channels.layers import get_channel_layer
    cl = get_channel_layer()
    await cl.group_send('chat_lobby', {"type": "chat_message", "message": 'ligma cope'})
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})

def login_view(request):
    """Handles both the login page and login logic"""
    # Taken from
    # https://stackoverflow.com/questions/16750464/django-redirect-after-login-not-working-next-not-posting
    state = "Please log in below..."
    username = password = ''

    redirect_url = ""

    if request.GET:
        redirect_url = request.GET['redirect_url']

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if redirect_url == "":
                    return redirect('/')  # Default "landing page"
                return redirect(redirect_url)
            # FIXME: do we need this?
            state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'login.html', {
        'state': state,
        'username': username,
        'redirect_url': redirect_url,
    })


@login_required()
def services(request):
    """Shows user's team's services and credentials"""
    services_data = Service.objects.values()  # Every team should have one of every service
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
