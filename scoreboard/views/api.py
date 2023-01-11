"""Views for the API"""
# pylint: disable=too-many-ancestors
# ViewSets have "too many ancestors", but cope

from rest_framework import viewsets

from scoreboard.models import Credential
from scoreboard.serializers import CredentialSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    """Handles views for api/credential URL"""
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    # TODO: add auth requirement
