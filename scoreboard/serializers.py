"""Serializers used for the API"""
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Score, Credential


# I don't know if this actually does anything?
class BulkCreateListSerializer(serializers.ListSerializer):
    """Exists to override list create to use bulk_create for performance"""
    # This is here so the IDE doesn't complain; might not be needed

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as error:
            raise ValidationError(error) from error

        return result


class ScoreSerializer(serializers.ModelSerializer):
    """Serializes Score objects"""
    class Meta:
        model = Score
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer


class CredentialSerializer(serializers.ModelSerializer):
    """Serializes Credential objects"""
    class Meta:
        model = Credential
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer
