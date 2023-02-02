# chat/routing.py
from django.urls import re_path

from scoreboard import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.DashboardConsumer.as_asgi())
]

