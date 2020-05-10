from rest_framework import serializers

from .models import Metadata, Datum
from application.models import Application
from device.models import Device

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class DatumSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=False)

    class Meta:
        model = Datum
        exclude = ('application', 'device')

    def create(self, validated_data):
        metadata_data = validated_data.pop('metadata')
        metadata = Metadata.objects.create(**metadata_data)

        application, application_created = Application.objects.get_or_create(id=validated_data.get('app_id'))
        device, device_created = Device.objects.get_or_create(id=validated_data.get('dev_id'))

        datum = Datum.objects.create(metadata=metadata, application=application, device=device, **validated_data)

        return datum
