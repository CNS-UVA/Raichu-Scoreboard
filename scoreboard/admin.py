"""Docstring here so Pylint doesn't complain"""
from django.contrib import admin

from .models import User, Team, Service, TeamService, Score, Credential

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(TeamService)
admin.site.register(Score)
admin.site.register(Credential)
