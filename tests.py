import urllib.request, json
from urllib.request import urlopen
import datetime


# URL = "https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json"

# response = urlopen(URL)
# data = json.loads(response.read().decode("utf-8"))
# itineraries = data['itineraries']
# legs = data['legs']

# # for item in itineraries:
# #   print(item)

# for item in legs:
#   # print(item)
#   print(item['stops'])




# datetime in string format for may 25 1999
input = "2020-10-31T15:35"

# format
# input = '2021/05/25'
format = '%Y-%m-%dT%H:%M'

# convert from string format to datetime format
datetime = datetime.datetime.strptime(input, format)

print(datetime)
