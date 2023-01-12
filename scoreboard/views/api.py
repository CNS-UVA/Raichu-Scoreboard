"""Views for the API"""
# pylint: disable=too-many-ancestors
# ViewSets have "too many ancestors", but cope

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from scoreboard.models import Credential, Score
from scoreboard.serializers import CredentialSerializer, ScoreSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    """Handles views for api/credentials URL"""
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [IsAdminUser]


class ScoreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """Handles views for api/scores URL"""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAdminUser]
