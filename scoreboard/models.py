"""Models for Scoreboard"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    """Team model. Does not actually store member Users"""
    name = models.CharField(max_length=100)

    # Make this separate from primary key so we can independently control it
    team_id = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.team_id})'


class User(AbstractUser):
    """User model"""
    # Team allowed to be nullable to allow team-less superuser lol
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)


class Service(models.Model):
    """Stores information for a given service e.g. FTP, SSH"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class TeamService(models.Model):
    """Stores data about a specific team's service"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    ip = models.CharField(max_length=15)
    port = models.IntegerField()

    def __str__(self):
        return f'{self.team} - {self.service}'


class Score(models.Model):
    """Reflects a single check on a team's service. Entries produced by score bot"""
    team_service = models.ForeignKey(TeamService, on_delete=models.CASCADE)
    round = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=200)


class Credential(models.Model):
    """Credential model.

    Stores credentials provided by users so we can check systems?
    TODO: Chase what does this do
    """
    service = models.ForeignKey(TeamService, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
