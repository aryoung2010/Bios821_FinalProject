from soccer_geocode import MapBoxGeocoder

class ConstrainedGeocoder(MapBoxGeocoder):

    def __init__(self, type):
        super().__init__()
        self._type = type

    @property
    def type(self):
        return self._type

    @property
    def con_geocode(self):
        for i in self.words:
            response = requests.get(
                "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?types={}access_token={}".format(i, self._type,self.mappass))
            data = response.json()
            self.long.append(data['features'][0]['center'][0])
            self.lat.append(data['features'][0]['center'][1])
