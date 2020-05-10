from rest_framework import viewsets, permissions

from .models import Metadata, Datum
from .serializers import MetadataSerializer, DatumSerializer

class MetadataViewSet(viewsets.ModelViewSet):
    serializer_class = MetadataSerializer

    def get_queryset(self):
        queryset = Metadata.objects. \
                   select_related('datum',). \
                   all()

        return queryset

class DatumViewSet(viewsets.ModelViewSet):
    serializer_class = DatumSerializer
    ordering_fields = ('id',)
    filter_fields = ('application', 'device', 'hardware_serial',)

    def get_queryset(self):
        queryset = Datum.objects. \
                   select_related('metadata', 'application', 'device',). \
                   all()

        return queryset
