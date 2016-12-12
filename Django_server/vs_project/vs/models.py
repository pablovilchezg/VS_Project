from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a user model instance
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    # ImageField uses pil: Python Imaging Library - it must be installed
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'points of interest'
