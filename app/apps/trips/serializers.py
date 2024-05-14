from rest_framework import serializers
from .models import Trip, TripDate
from apps.users.serializers import UserSerializer


class TripDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDate
        fields = '__all__'


class TripDetailsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    editors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'updatedAt')


# class TripEditorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TripEditor
#         fields = '__all__'
