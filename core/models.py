from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Profile(models.Model):
  username = models.CharField(max_length = 16)
  gender = models.CharField(max_length = 7)
  linkedIn_id = models.CharField(primary_key=True, max_length = 20)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)
  location  = models.PointField(null=True, blank=True)
  objects = models.GeoManager()