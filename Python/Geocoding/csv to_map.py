from unittest import skip
import pandas as pd
import folium
from folium import plugins

data=pd.read_csv('1.csv', encoding='ansi',  delimiter=',',low_memory=False)
df=pd.DataFrame(data)
df['lat']=pd.to_numeric(df['lat'])
df['lon']=pd.to_numeric(df['lon'])
map=folium.Map(
    location=[df['lat'].mean(),df['lon'].mean()],
    zoom_start=8,
    control_scale=True)
marker_cluster=plugins.MarkerCluster().add_to(map)

for name,row in df.iterrows():
    iframe=folium.IFrame('<b><h2>{name}</h2></b><hr><br>電腦編號:{addr}<br>村里別:{tele}<br>可容納人數:{web}人'.format(
            name=row['地址'],
            addr=row['電腦編號'],
            tele=row['村里別'],
            web=row['可容納人數']))
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(iframe,min_width=400, max_width=400),
        tooltip='{name}'.format(name=row['地址'])).add_to(marker_cluster)
map.save('KS.html')