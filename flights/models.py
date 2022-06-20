from django.db import models

# Create your models here.
class Leg(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  departure_airport = models.CharField(max_length=255, blank=True, null=True)
  arrival_airport = models.CharField(max_length=255, blank=True, null=True)
  departure_time = models.DateTimeField()
  arrival_time = models.DateTimeField()
  stops = models.IntegerField(default=0)
  airline_name = models.CharField(max_length=255, blank=True, null=True)
  airline_id = models.CharField(max_length=255, blank=True, null=True)
  duration_mins = models.IntegerField(default=0)

  def __str__(self):
    return self.id

class Itinerarie(models.Model):
  id = models.CharField(max_length=200, primary_key=True)
  legs = models.ManyToManyField(Leg)
  price = models.CharField(max_length=255, null=True, blank=True)
  agent = models.CharField(max_length=255, blank=True, null=True)
  agent_rating = models.FloatField(null=True, blank=True, default=0.0)

  def __str__(self):
    return self.id
