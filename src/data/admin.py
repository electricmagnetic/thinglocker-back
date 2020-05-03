from django.contrib import admin

from .models import Datum, Metadata

admin.site.register(Datum)
admin.site.register(Metadata)
