"""Models for Scoreboard"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    """Team model. Does not actually store member Users"""
    name = models.CharField(max_length=100)

    # Make this separate from primary key so we can independently control it
    team_id = models.IntegerField()


class User(AbstractUser):
    """User model"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Service(models.Model):
    """Stores information for a given service e.g. FTP, SSH"""
    name = models.CharField(max_length=100)


class TeamService(models.Model):
    """Stores data about a specific team's service"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    port = models.IntegerField()


class Credential(models.Model):
    """Credential model.

    Stores credentials provided by users so we can check systems?
    TODO: Chase what does this do
    """
    service = models.ForeignKey(TeamService, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
