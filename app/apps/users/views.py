from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters
from .serializers import UserSerializer
from apps.trips.models import Trip
from django.shortcuts import get_object_or_404
from .models import CustomUser


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'perPage'
    max_page_size = 25


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['lastName', 'firstName', 'middleName']

    def get_queryset(self):
        trip_id = self.kwargs['trip_id']
        trip = get_object_or_404(Trip, pk=trip_id)
        owner = trip.owner
        editors = trip.editors.all()
        all_users = CustomUser.objects.all().order_by(
            'lastName', 'firstName', 'middleName')
        queryset = all_users.exclude(id=owner.id).exclude(
            id__in=editors.values_list('id', flat=True))
        return queryset
