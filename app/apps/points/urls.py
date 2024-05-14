from django.urls import path
from .views import PointsList, PointDetails, PointPhotosList, PointPhotoDetails, DeletePhotos, PointSampleViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'pointsamples', PointSampleViewSet)

urlpatterns = [
    path('trip-points/<int:trip_id>/', PointsList.as_view(),
         name='get trip points list/post new trip point'),
    path('point/<int:pk>/', PointDetails.as_view(),
         name='get/patch/put/delete specific point'),
    path('point/<int:point_id>/photos/', PointPhotosList.as_view(),
         name='get point photos list/post new point photo'),
    path('point-photo/<int:pk>/', PointPhotoDetails.as_view(),
         name='get/patch/put/delete specific photo'),
    path('point/<int:pk>/delete-photos', DeletePhotos.as_view(),
         name='delete all point photos'),
]

urlpatterns += router.urls
