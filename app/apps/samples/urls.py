from rest_framework import routers
from .views import CharacteristicViewSet, SampleViewSet, SampleCharacteristicViewSet

router = routers.SimpleRouter()
router.register(r'characteristics', CharacteristicViewSet)
router.register(r'samples', SampleViewSet)
router.register(r'samplecharacteristics', SampleCharacteristicViewSet)

urlpatterns = router.urls
