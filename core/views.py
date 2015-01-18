from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.measure import D
from django.contrib.gis import geos
from core.models import Profile
from utility import *

# Create your views here.
def index(request):
  saveSubmitData(request)
  return render(request, 'core.html')

def listPeople(request):
  linkedinId = request.session['id']
  try:
    p = Profile.objects.get(linkedinId = linkedinId)
  except Profile.DoesNotExist:
    pass
  else:
    current_point = p.location
    friends = Profile.objects.filter(location__distance_lte=(current_point, D(km=100)))
    print 1
    return render(request,'friends.html', {'friends' : friends}) 
  return render(request, 'friends.html')