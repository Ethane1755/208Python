from winreg import HKEY_CLASSES_ROOT
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

locator = Nominatim(user_agent='name_of_your_app')
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
print('強烈建議使用原文地名')
a = input('please input the place you want to search:')
print('If you want to get',a,"\'s Lat/Long, press x. If you want its address, press y.")
b = input()
location = locator.geocode(a)
addr = location.address
lat_lon = location.latitude, location.longitude
if b == 'x':
    print(lat_lon)
else:
    print(addr)