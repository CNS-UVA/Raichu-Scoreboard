"""Serializers used for the API"""
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from scoreboard.models import Score, Credential, Service, Team


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializes Service objects.
    """

    class Meta:
        model = Service
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializes Service objects.
    """

    class Meta:
        model = Team
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer


class CredentialSerializer(serializers.ModelSerializer):
    """Serializes Credential objects"""

    class Meta:
        model = Credential
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer


class BulkCreateListSerializer(serializers.ListSerializer):
    """Overrides ScoreSerializer list create to use more efficient bulk_create"""

    def update(self, instance, validated_data):
        # We don't need to use update, but the IDE complains if it's not here
        pass

    def create(self, validated_data):
        # Note: self.child is always ScoreSerializer. This uses ScoreSerializer to
        # create individual Score objects, then uses bulk_create to put them into
        # the database with only 1 SQL call.
        new_scores = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(new_scores)
        except IntegrityError as error:
            raise ValidationError(error) from error

        return new_scores


class ScoreSerializer(serializers.ModelSerializer):
    """Serializes Score objects"""

    def create(self, validated_data):
        instance = Score(**validated_data)

        # If creating multiple, don't save here so we can bulk create later
        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    class Meta:
        model = Score
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer
