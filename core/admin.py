from django.contrib import admin
from core.models import *
# Register your models here.
#class Profile(admin.ModelAdmin):
#	list_display = ('linkedinId', 'firstName', 'lastName')

admin.site.register(Profile)
admin.site.register(Invite)

