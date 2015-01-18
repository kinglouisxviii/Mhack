from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Profile(models.Model):
  firstName = models.CharField(max_length = 30, null= True)
  lastName = models.CharField(max_length = 30, null = True)
  industry = models.CharField(max_length = 40, null = True)
  linkedinId = models.CharField(primary_key=True, max_length = 20)
  isActive = models.BooleanField(default = False)
  location  = models.PointField(null=True, blank=True)
  objects = models.GeoManager()

class Invite(models.Model):
  id = models.IntegerField(null = False, primary_key = True, default = 0)
  time = models.CharField(max_length = 5, null = True)
  subject = models.CharField(max_length = 100, null = True)
  linkedinId = models.CharField(max_length = 20, null = True)
  place = models.CharField(max_length = 25, null = True)
  #countOfPeopleComing = models.DecimalField(max_digits=None, decimal_places=None, null = True)
  objects = models.GeoManager()