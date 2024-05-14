from rest_framework import serializers
from .models import Characteristic, SampleCharacteristic, Sample


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Sample
        fields = '__all__'


class SampleCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleCharacteristic
        fields = '__all__'
