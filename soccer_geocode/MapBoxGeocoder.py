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
        self.map_pass = os.environ.get('MAP_PASS')
        self.url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
        self.countries = countries
        print("MapBoxGeocoder initiated")


        @property
        def charge(self):
            return self._charge
## Check connection
def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()