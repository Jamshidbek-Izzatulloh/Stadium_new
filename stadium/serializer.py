from rest_framework import serializers 
from .models import (OwnerModel, StadiumModel, BookingModel)

class OwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = '__all__'

class StadiumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = '__all__'

class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__'

