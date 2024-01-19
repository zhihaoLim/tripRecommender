from django.contrib import admin 
# Register your models here.

from .models import Traveler, TouristSpot

admin.site.register(Traveler)
admin.site.register(TouristSpot)