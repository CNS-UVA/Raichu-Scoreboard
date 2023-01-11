from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from scoreboard.models import Credential
from scoreboard.serializers import CredentialSerializer


def mickey(request):
    # TODO: password protect?
    serializer = CredentialSerializer(Credential.objects.all(), many=True)
    # TODO: investigate why safe needs to be False
    return JsonResponse(serializer.data, safe=False)

def TheFunction(request):
    return None