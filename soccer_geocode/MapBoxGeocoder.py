#### Import packages
import sqlite3
import os
import requests
from sqlite3 import Error

### Set API Key



### Connect to the database
connection = sqlite3.connect("database.sqlite")

# cursor
crsr = connection.cursor()

class MapBoxGeocoder:
    '''A class of geocoding tools for the Mapbox API'''

    def __init__(self, MAP_PASS, countries):
        self.mappass = os.environ.get('MAP_PASS')
        self.url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
        self.countries = countries
        self.ids = []
        self.words = []
        self.lat = []
        self.long = []
        print("MapBoxGeocoder initiated")

    @property
    def label_countries(self):
        for a,b in self.countries:
            self.words.append(b)
            self.ids.append(a)

    @property
    def geocode(self):
        for i in self.words:
            response = requests.get(
            "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token={}".format(i, self.mappass))
            data = response.json()
            self.long.append(data['features'][0]['center'][0])
            self.lat.append(data['features'][0]['center'][1])

    @property
    def package_table(self):
        data_tuples = list(zip(self.ids, self.words, self.lat, self.long))
        return data_tuples
