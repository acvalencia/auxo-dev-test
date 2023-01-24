from django.contrib import admin
from flights.models import Airport, Airline, Agent, Itinerarie, Leg

admin.site.site_header = 'Administration'
# Register your models here.
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(Agent)
admin.site.register(Itinerarie)
admin.site.register(Leg)
