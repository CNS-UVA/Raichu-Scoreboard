# pylint: disable=invalid-name
# COPE:
"""Views for the API"""
from django.http import JsonResponse

from scoreboard.models import Credential
from scoreboard.serializers import CredentialSerializer


def mickey(request):
    """View for reading all Credential objects"""
    # TODO: password protect? ligma cope
    serializer = CredentialSerializer(Credential.objects.all(), many=True)
    # TODO: investigate why safe needs to be False
    return JsonResponse(serializer.data, safe=False)


def TheFunction(request):
    """View for creating new Score objects"""
    return None
