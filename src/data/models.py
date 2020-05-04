from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class Metadata(models.Model):
    """ Metadata associated with a given data point """

    time = models.DateTimeField()
    frequency = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    modulation = models.CharField(max_length=4, null=True, blank=True)
    data_rate = models.CharField(max_length=8, null=True, blank=True)
    bit_rate = models.IntegerField(null=True, blank=True)
    coding_rate = models.CharField(max_length=3, null=True, blank=True)
    gateways = JSONField(null=True, blank=True)
    latitude = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=7)
    longitude = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=7)
    altitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return ("%s" % (self.time.strftime("%Y-%m-%d %H:%M:%S")))

    class Meta:
        ordering = ['-time']
        verbose_name = 'metadata'
        verbose_name_plural = 'metadata'

class Datum(models.Model):
    """ Data point submitted by the Things Network """

    app_id = models.CharField(max_length=36)
    dev_id = models.CharField(max_length=36)
    hardware_serial = models.CharField(max_length=16, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    counter = models.IntegerField(null=True, blank=True)
    is_retry = models.BooleanField(null=True)
    confirmed = models.BooleanField(null=True)
    payload_raw = models.CharField(max_length=128, null=True, blank=True)
    payload_fields = JSONField(null=True, blank=True)
    metadata = models.OneToOneField(Metadata, on_delete=models.CASCADE)
    downlink_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return ("%s" % (self.id))

    class Meta:
        ordering = ['-id',]
        verbose_name = 'datum'
        verbose_name_plural = 'data'
