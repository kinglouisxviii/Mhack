from django.shortcuts import render
from django.http import HttpResponse
from utility import *

# Create your views here.
def index(request):
  saveSubmitData(request)
  return render(request, 'core.html')