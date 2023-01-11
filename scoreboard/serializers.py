from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from rest_framework.parsers import JSONParser
from .models import Score, Credential


# I don't know if this actually does anything?
class BulkCreateListSerializer(serializers.ListSerializer):
    # This is here so the IDE doesn't complain; might not be needed
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer
