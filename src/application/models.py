from django.db import models

class Application(models.Model):
    """ A particular TTN application """

    id = models.CharField(max_length=36, primary_key=True)

    def __str__(self):
        return ("%s" % (self.id))
