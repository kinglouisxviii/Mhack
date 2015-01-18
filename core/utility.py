from django.core.exceptions import *
from core.models import *
from django.contrib.gis.geos import GEOSGeometry

def saveSubmitData(request):
  if request.method == 'POST':
    lat_val = request.POST['lat']
    lng_val = request.POST['lng']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    industry = request.POST['industry']
    linkedinId = request.POST['linkedinId']
    request.session['id'] = linkedinId
    point = GEOSGeometry('POINT(%s %s)' % (lat_val, lng_val))
    try:
      print "try"
      p = Profile.objects.get(linkedinId = linkedinId)
      print "finish try"
    except Profile.DoesNotExist:
      print "enter create process"
      newProfile = Profile(firstName = firstName,
                                          lastName = lastName,
                                          linkedinId = linkedinId,
                                          industry = industry,
                                          location = point,
                                          isActive = True)
      newProfile.save()
    else:
      print "enter save process"
      p.location = point
      p.isActive = True
      p.save()
      print "save success"
    