from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Itinerarie

# Create your views here.
def index(request):

    filter = request.GET.get("minrating")
    if filter is not None:
        itineraries = Itinerarie.objects.filter(agent_rating__gte=filter)
    else:
        itineraries = Itinerarie.objects.all()

    return render(
        request,
        'index.html',
        context = {
            'itineraries': itineraries,
        })
