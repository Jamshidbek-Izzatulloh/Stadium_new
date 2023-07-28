from rest_framework import serializers 
from .models import (OwnerModel, StadiumModel, BronedStadiumModel)

class OwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = '__all__'

class StadiumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = '__all__'

class BronedStadiumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BronedStadiumModel
        fields = '__all__'

