"""Models for Scoreboard"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Service(models.Model):
    """Stores information for a given service e.g. FTP, SSH"""
    name = models.CharField(max_length=100)
    # TODO: get a better name for this field
    ip_suffix = models.CharField(max_length=15)  # Should get concatenated w/ team's subnet
    port = models.IntegerField()

    def __str__(self):
        return f'{self.name} service'


class Team(AbstractUser):
    """
    Team model.
    Teams each have one user account.
    Note that all fields are nullable to support creating superusers.
    """
    name = models.CharField(max_length=100, null=True)

    # Make this separate from primary key, so we can independently control it
    team_num = models.IntegerField(null=True)

    # TODO: come up with a better name for this field
    subnet = models.CharField(max_length=15, null=True)
    # We don't need to have Services as a field because it's assumed all teams have every Service

    def __str__(self):
        return f'{self.username}'


class Score(models.Model):
    """Reflects a single check on a team's service. Entries produced by score bot"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    round = models.IntegerField()
    timestamp = models.DateTimeField()
    passed = models.BooleanField()  # Should only ever be pass/fail for now
    message = models.TextField()

    def __str__(self):
        return f'Score for {self.team}, {self.service}, round {self.round}'


class Credential(models.Model):
    """Credential model.

    Stores credentials provided by users so we can check systems?
    TODO: Chase what does this do
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'Credential for {self.team}, {self.service}'
