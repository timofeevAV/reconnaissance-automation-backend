from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include('apps.trips.urls')),
        path('', include('apps.points.urls')),
        path('', include('apps.users.urls')),
        path('', include('apps.samples.urls')),
    ])),
    path('auth/', include([
        path('', include('djoser.urls')),
        path('', include('djoser.urls.jwt')),
    ])),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
