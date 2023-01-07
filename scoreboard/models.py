"""Models for Scoreboard"""
from django.db import models

class Team(models.Model):
    """Team model"""
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    members = models.CharField(max_length=300)
    contact = models.EmailField()

class Credential(models.Model):
    """Credential model.

    Stores credentials provided by users so we can check systems?
    TODO: Chase what does this do
    """
    team_id = models.IntegerField()
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    port = models.IntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Service(models.Model):
    """Stores information for a given service e.g. FTP, SSH"""
    service_name = models.CharField(max_length=100)

class TeamService(models.Model):
    """Stores data about a specific team's service"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

