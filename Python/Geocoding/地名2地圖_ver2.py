# coding=utf-8#
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium.plugins import MarkerCluster

locator = Nominatim(user_agent='myGeocoder')
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

print('強烈建議使用原文地名')
a = input('please input the place you want to search:')
locationa = locator.geocode(a)
lat_lon = locationa.latitude, locationa.longitude
Map = folium.Map(tiles = 'stamentoner',location=(lat_lon),zoom_start=10) 

b = input('Do you want to add another place to the map? ')
cluster = MarkerCluster().add_to(Map)
folium.Marker(lat_lon,popup=a).add_to(cluster)

while b == "yes":
        c = input('please input the place you want to search:')
        locationc = locator.geocode(c)
        lat_lonc = [locationc.latitude, locationc.longitude]
        folium.Marker(lat_lonc,popup=c).add_to(cluster)
        b = input('Do you want to add another place to the map? ')  
else:        
        print('Thank you.')
        Map.save('a.html')