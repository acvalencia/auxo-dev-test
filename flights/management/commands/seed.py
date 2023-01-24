from flights.models import Airport, Airline, Agent, Itinerarie, Leg
from django.core.management.base import BaseCommand
from urllib.request import urlopen
import json
import datetime

URL = "https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json"
format = '%Y-%m-%dT%H:%M'

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print('clearing data...')
    Leg.objects.all().delete()
    Itinerarie.objects.all().delete()


def create_data():
    """Creates an address object combining different elements from the list"""
    print("Creating data")
    response = urlopen(URL)
    data = json.loads(response.read().decode("utf-8"))
    itineraries = data['itineraries']
    legs = data['legs']

    for item in legs:

      # Create Airport object
      # Created = false if object exists
      departure_airport, dep_created = Airport.objects.get_or_create(id=item['departure_airport'])
      arrival_airport, arri_created  = Airport.objects.get_or_create(id=item['arrival_airport'])

      if dep_created:
        departure_airport.save()

      if arri_created:
        arrival_airport.save()

      departure_datetime = datetime.datetime.strptime(item['departure_time'], format)
      arrival_datetime = datetime.datetime.strptime(item['arrival_time'], format)

      # Craete Airline
      airline, air_created = Airline.objects.get_or_create(id = item['airline_id'], name = item['airline_name'])
      if air_created:
        airline.save()

      # Create Leg Object
      leg = Leg(
        id =  item['id'],
        departure_airport = departure_airport,
        arrival_airport = arrival_airport,
        departure_time = departure_datetime,
        arrival_time = arrival_datetime,
        stops = item['stops'],
        airline = airline,
        duration_mins = item['duration_mins']
      )
      leg.save()

    for item in itineraries:

      agent = Agent(agent = item['agent'],
                    agent_rating = item['agent_rating'])
      agent.save()

      itinerarie = Itinerarie(
        id = item['id'],
        price = item['price'],
        agent = agent
      )
      itinerarie.save()

      for item_leg in item['legs']:
        leg = Leg.objects.get(id=item_leg)
        itinerarie.legs.add(leg)


    print('Save Flights to database')
    return True

def run_seed(self, mode):
    """ Seed database based on mode
    :param mode: refresh / clear
    :return:
    """

    print('Running seed database')

    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_data()
