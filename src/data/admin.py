from django.contrib import admin

from .models import Datum, Metadata

class DatumAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'application', 'device', 'payload_raw', 'metadata')
    list_filter = ('application', 'device', 'metadata__time')
    readonly_fields = ('metadata',)

class MetadataAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'datum')

admin.site.register(Datum, DatumAdmin)
admin.site.register(Metadata, MetadataAdmin)
