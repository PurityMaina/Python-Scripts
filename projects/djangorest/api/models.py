from django.db import models

class Bucketlist(models.Model):
    """This class represents the buscketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        """return a human readable representation of the model instance."""
        return "{}".format(self.name)

    pass

# Create your models here.
