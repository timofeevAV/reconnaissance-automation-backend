from rest_framework import serializers
from .models import Point, PointPhoto, PointSample
from apps.samples.serializers import SampleSerializer


class PointPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointPhoto
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    photos = PointPhotoSerializer(
        many=True,
        read_only=True,
    )

    samples = SampleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Point
        fields = '__all__'


class PointSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointSample
        fields = '__all__'
