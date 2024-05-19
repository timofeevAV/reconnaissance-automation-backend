from rest_framework import serializers
from .models import Trip, TripDate
from apps.users.serializers import UserSerializer
from apps.points.serializers import PointCoordsSerializer

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
        

class TripInBoundsSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'name', 'points']

    def get_points(self, obj):
        points = obj.points.exclude(latitude__isnull=True, longitude__isnull=True)
        return PointCoordsSerializer(points, many=True).data