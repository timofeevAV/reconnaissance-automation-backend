from django.urls import path
from .views import UsersList

urlpatterns = [
    path('users/<int:trip_id>/', UsersList.as_view()),
]
