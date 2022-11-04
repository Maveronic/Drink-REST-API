from .models import Drink
from rest_framework import serializers


# Created a serializer which serializes the Drink model
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'description')
