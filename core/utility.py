from django.core.exceptions import *
from core.models import *

def saveSubmitData(request):
  if request.method == 'POST':
    lat_val = request.POST['lat']
    lng_val = request.POST['lng']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    industry = request.POST['industry']
    linkedinId = request.POST['linkedinId']
    try:
      print "try"
      p = Profile.objects.get(linkedinId = linkedinId)
      print "finish try"
    except Profile.DoesNotExist:
      print "enter create process"
      newProfile = Profile(firstName = firstName,
                                          lastName = lastName,
                                          linkedinId = linkedinId,
                                          latitude = lat_val,
                                          longtitude = lng_val,
                                          industry = industry,
                                          isActive = True)
      newProfile.save()
    else:
      print "enter save process"
      p.latitude = lat_val
      p.longtitude = lng_val
      p.isActive = True
      p.save()
      print "save success"
    