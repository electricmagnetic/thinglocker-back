from django.db import models

class Device(models.Model):
    """ A particular TTN device """

    id = models.CharField(max_length=36, primary_key=True)

    def __str__(self):
        return ("%s" % (self.id))
