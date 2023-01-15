"""Docstring here so Pylint doesn't complain"""
from django.contrib import admin

from .models import Team, Service, Score, Credential

# Register your models here.
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(Score)
admin.site.register(Credential)
