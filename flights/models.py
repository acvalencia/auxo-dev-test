from django.db import models

# Create your models here.
class Leg(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  departure_airport = models.CharField(max_length=255, blank=True, null=True) # FORING KEY
  arrival_airport = models.CharField(max_length=255, blank=True, null=True)   # FORING KEY
  departure_time = models.DateTimeField()
  arrival_time = models.DateTimeField()
  stops = models.IntegerField(default=0)
  airline_name = models.CharField(max_length=255, blank=True, null=True) # REMOVE THIS
  airline_id = models.CharField(max_length=255, blank=True, null=True)   # FORING KEY
  duration_mins = models.IntegerField(default=0)

  def __str__(self):
    return self.id

# class Airport(models.Model):
#   id = models.CharField(max_length=100, primary_key=True)

#   def __str__(self):
#     return self.id

# class Airline(models.Model):
#   id = models.CharField(max_length=100, primary_key=True)
#   name = models.CharField(max_length=255, blank=True, null=True)

#   def __str__(self):
#     return self.name

class Agent(models.Model):
  agent = models.CharField(max_length=255, primary_key=True)
  agent_rating = models.FloatField(null=True, blank=True, default=0.0)

  def __str__(self):
    return self.agent

class Itinerarie(models.Model):
  id = models.CharField(max_length=200, primary_key=True)
  legs = models.ManyToManyField(Leg)
  price = models.CharField(max_length=255, null=True, blank=True)
  agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

  def __str__(self):
    return self.id
