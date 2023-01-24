from flights.models import Airport, Airline, Agent, Itinerarie, Leg
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

# ViewSets define the view behavior.
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

# Serializers define the API representation.
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

# ViewSets define the view behavior.
class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

# Serializers define the API representation.
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

# ViewSets define the view behavior.
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# Serializers define the API representation.
class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'

# ViewSets define the view behavior.
class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

# Serializers define the API representation.
class ItinerarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerarie
        fields = '__all__'

# ViewSets define the view behavior.
class ItinerarieViewSet(viewsets.ModelViewSet):
    queryset = Itinerarie.objects.all()
    serializer_class = ItinerarieSerializer
