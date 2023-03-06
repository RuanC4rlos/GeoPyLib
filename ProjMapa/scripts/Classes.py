import folium

class Map:
    def __init__(self, center, zoom):
        self.center = center
        self.zoom = zoom
        self.layers = []

    def add_layer(self, layer):
        self.layers.append( layer )

    def remove_layer(self, layer):
        self.layers.remove( layer )

    def set_zoom(self, zoom):
        self.zoom = zoom

    def set_center(self, center):
        self.center = center

    def create_marcador(self, lat, lon, titulo):
        marker = folium.Marker( location=[lat, lon], popup=titulo )
        return marker

    def show(self):
        m = folium.Map( location=[self.center[0], self.center[1]], zoom_start=self.zoom )
        for layer in self.layers:
            m.add_child( layer )
        return m
    
    def create_map(self):
        m = folium.Map(location=self.center, zoom_start=self.zoom)
        for layer in self.layers:
            m.add_child(layer)
        html = m.get_root().render()
        return html
    
import math

class Coordinate:
    def __init__(self, lat, lon, alt=None):
        self.latitude = lat
        self.longitude = lon
        self.altitude = alt
        
    def distance(self, other):
        # calcula a distância entre esta coordenada e outra, usando o algoritmo especificado
        # fórmula de Haversine para distância entre dois pontos em uma esfera (como a Terra)
        R = 6371  # raio médio da Terra em quilômetros
        d_lat = math.radians(other.latitude - self.latitude)
        d_lon = math.radians(other.longitude - self.longitude)
        lat1 = math.radians(self.latitude)
        lat2 = math.radians(other.latitude)
        a = math.sin(d_lat/2)**2 + math.sin(d_lon/2)**2 * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c
import requests

class Location:
    def __init__(self, name, address, latitude, longitude):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def set_weather(self, api_key,lat,lon):
        #url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'main' in data:
            self.temperature = data["main"]["temp"]
            self.humidity = data["main"]["humidity"]
            self.pressure = data["main"]["pressure"]
        else:
            self.temperature = None
            self.humidity = None
            self.pressure = None

    def get_coordinates(self):
        return self.latitude, self.longitude
import requests
import json

class OSMGeocoder:
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"

    def geocode(self, address):
        params = {
            "q": address,
            "format": "json",
            "addressdetails": 1
        }
        response = requests.get(self.base_url, params=params)
        data = json.loads(response.text)
        if data:
            location = data[0]
            return location["lat"], location["lon"]
        else:
            return None
     
    def reverse_geocode(self, latitude, longitude):
        self.url = "https://nominatim.openstreetmap.org/reverse"
        try:
            response = requests.get(
                self.url,
                params={"format": "json", "lat": latitude, "lon": longitude}
            )
            if response.ok:
                data = response.json()
                address = data.get("address")
                if address:
                    state = address.get("state")
                    if not state:
                        state = address.get("state_district")
                    if not state:
                        state = address.get("region")
                    if not state:
                        state = address.get("county")
                    if not state:
                        state = address.get("city")
                    if not state:
                        state = address.get("town")
                    if not state:
                        state = address.get("village")
                    if not state:
                        state = address.get("hamlet")
                    if not state:
                        state = address.get("island")
                    
                    road = address.get("road")
                    if road:
                        return state, road
                    else:
                        return None, None
                else:
                    return None, None
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error}")
        except requests.exceptions.RequestException as error:
            print(f"Request error: {error}")