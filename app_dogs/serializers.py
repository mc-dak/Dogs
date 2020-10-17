from rest_framework import serializers
from app_dogs.models import Dogs


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dogs
        fields = ('name', 'birthday', 'arrived_at', 'weight', 'height', 'special', 'shelter')
