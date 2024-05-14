from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'lastName', 'firstName', 'middleName', 'role']
