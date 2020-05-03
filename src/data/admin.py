from django.contrib import admin

from .models import Datum, Metadata

class DatumAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'app_id', 'dev_id', 'payload_raw', 'metadata')
    list_filter = ('app_id', 'dev_id', 'metadata__time')
    readonly_fields = ('metadata',)

class MetadataAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'datum')

admin.site.register(Datum, DatumAdmin)
admin.site.register(Metadata, MetadataAdmin)
