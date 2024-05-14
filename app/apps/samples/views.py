from rest_framework import viewsets
from .models import Characteristic, Sample, SampleCharacteristic
from .serializers import CharacteristicSerializer, SampleSerializer, SampleCharacteristicSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleCharacteristicViewSet(viewsets.ModelViewSet):
    queryset = SampleCharacteristic.objects.all()
    serializer_class = SampleCharacteristicSerializer

    @action(detail=False, methods=['delete'])
    def delete_by_composite_key(self, request):
        try:
            characteristic_id = request.data.get('characteristic_id')
            sample_id = request.data.get('sample_id')

            sample_characteristic_to_delete = SampleCharacteristic.objects.filter(
                сharacteristic_id=characteristic_id, sample_id=sample_id).first()

            if sample_characteristic_to_delete:
                sample_characteristic_to_delete.delete()
                return Response({'message': 'SampleCharacteristic deleted successfully'})
            else:
                return Response({'message': 'SampleCharacteristic not found'}, status=404)

        except Exception as e:
            return Response({'error': str(e)}, status=400)
