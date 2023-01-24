from django.urls import path, include
from rest_framework import routers
from . import views
from . import serializers

router = routers.DefaultRouter()
router.register(r'airports', serializers.AirportViewSet)
router.register(r'airlines', serializers.AirlineViewSet)
router.register(r'agents', serializers.AgentViewSet)
router.register(r'legs', serializers.LegViewSet)
router.register(r'itineraries', serializers.ItinerarieViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
