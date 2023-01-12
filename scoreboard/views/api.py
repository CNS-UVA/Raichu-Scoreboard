"""Views for the API"""
# pylint: disable=too-many-ancestors
# ViewSets have "too many ancestors", but cope

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from scoreboard.models import Credential, Score
from scoreboard.serializers import CredentialSerializer, ScoreSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    """Handles views for api/credentials URL"""
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [IsAdminUser]


class ScoreViewSet(viewsets.ModelViewSet):
    """Handles views for api/scores URL"""
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAdminUser]
