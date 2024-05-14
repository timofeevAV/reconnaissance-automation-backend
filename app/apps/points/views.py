from rest_framework import status, generics, viewsets
from .models import Point, PointPhoto, PointSample
from .serializers import PointSerializer, PointPhotoSerializer, PointSampleSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.trips.models import Trip


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'perPage'
    max_page_size = 25


class PointsList(generics.ListCreateAPIView):
    serializer_class = PointSerializer
    pagination_class = Pagination

    def get_queryset(self):
        trip = get_object_or_404(Trip, pk=self.kwargs['trip_id'])
        return trip.points.all()

    def post(self, request, trip_id, format=None):
        try:
            trip = Trip.objects.get(pk=trip_id)
        except Trip.DoesNotExist:
            return Response({'detail': 'Нет выезда с таким id'}, status=status.HTTP_400_BAD_REQUEST)
        point = Point.objects.create(trip=trip)
        serialized_point = PointSerializer(point)
        return Response(serialized_point.data, status=status.HTTP_201_CREATED)


class PointDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointPhotosList(generics.ListCreateAPIView):
    serializer_class = PointPhotoSerializer

    def get_queryset(self):
        point = get_object_or_404(Point, pk=self.kwargs['point_id'])
        return point.photos.all()

    def post(self, request, point_id, format=None):
        photos = request.FILES.getlist('photo')

        if point_id and photos:
            try:
                point = Point.objects.get(pk=point_id)
            except Point.DoesNotExist:
                return Response({'detail': 'Нет точки с таким id'}, status=status.HTTP_400_BAD_REQUEST)
            created_point_photos = []
            for photo in photos:
                photo_point_instance = PointPhoto.objects.create(
                    photo=photo, point=point)
                created_point_photos.append(photo_point_instance)
            serialized_photo_point = self.get_serializer(
                created_point_photos, many=True)
            return Response(serialized_photo_point.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PointPhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PointPhoto.objects.all()
    serializer_class = PointPhotoSerializer


class DeletePhotos(generics.DestroyAPIView):
    queryset = PointPhoto.objects.all()

    def destroy(self, request, *args, **kwargs):
        point_id = kwargs.get('pk')
        photos_to_delete = PointPhoto.objects.filter(point_id=point_id)

        if photos_to_delete.exists():
            photos_to_delete.delete()
            return Response({"detail": "Фото успешно удалены."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Для указанной точки фотографий не найдено."}, status=status.HTTP_404_NOT_FOUND)


class PointSampleViewSet(viewsets.ModelViewSet):
    queryset = PointSample.objects.all()
    serializer_class = PointSampleSerializer
