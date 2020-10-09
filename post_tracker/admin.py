from django.contrib import admin
from .models import Track, Statuses, TrackPoint, Country, City

admin.site.register(Track)
admin.site.register(Statuses)
admin.site.register(TrackPoint)
admin.site.register(Country)
admin.site.register(City)
