from rest_framework.routers import DefaultRouter

from data.views import MetadataViewSet, DatumViewSet

router = DefaultRouter()

router.register(r'datum', DatumViewSet, 'Datum')
router.register(r'metadata', MetadataViewSet, 'Metadata')
