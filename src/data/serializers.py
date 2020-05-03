from rest_framework import serializers

from .models import Metadata, Datum

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class DatumSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=False)

    class Meta:
        model = Datum
        fields = '__all__'

    def create(self, validated_data):
        metadata_data = validated_data.pop('metadata')

        metadata = Metadata.objects.create(**metadata_data)
        datum = Datum.objects.create(metadata=metadata, **validated_data)

        return datum
