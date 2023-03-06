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
