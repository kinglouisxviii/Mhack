from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.measure import D
from django.contrib.gis import geos
from core.models import Profile
from core.models import Invite
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
    invites = []
    for friend in friends : 
      try: 
        invite = Invite.objects.get(linkedinId = friend.linkedinId)
      except Invite.DoesNotExist:
        pass
      else:
        invites.append(invite)
        print 1
    return render(request,'friends.html', {'invites' : invites, 'friends' : friends}) 
  return render(request, 'friends.html')