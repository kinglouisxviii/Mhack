from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Profile(models.Model):
  firstName = models.CharField(max_length = 30, null= True)
  lastName = models.CharField(max_length = 30, null = True)
  industry = models.CharField(max_length = 40, null = True)
  linkedinId = models.CharField(primary_key=True, max_length = 20)
  latitude = models.FloatField(null=True, blank=True)
  longtitude = models.FloatField(null=True, blank=True)
  isActive = models.BooleanField(default = False)
  location  = models.PointField(null=True, blank=True)
  '''objects = models.GeoManager()'''