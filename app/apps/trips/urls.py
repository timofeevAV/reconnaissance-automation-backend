from django.urls import path
from .views import TripsListView, TripDetailsView, DeleteTripsView, TripDateDetailsView, TripDateListView, TripEditorView, TripDownloadView

urlpatterns = [
    path('trips/', TripsListView.as_view(),
         name='get trips list/post new trip'),
    path('trips/delete/', DeleteTripsView.as_view(),
         name='multiple delete trips'),
    path('trip/<int:pk>/', TripDetailsView.as_view(),
         name='get/patch/put/delete specific trip'),
    path('trip/<int:pk>/download/', TripDownloadView.as_view()),
    path('trip-editor/<int:pk>/<str:action>/', TripEditorView.as_view()),
    path('trip-dates/<int:trip_id>/', TripDateListView.as_view(),
         name='get trip dates list/post new trip date'),
    path('trip-date/<int:pk>/', TripDateDetailsView.as_view(),
         name='get/patch/put/delete specific trip date'),
]
