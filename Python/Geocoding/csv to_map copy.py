import pandas as pd
import folium
from folium import plugins

data=pd.read_csv('2.csv', encoding='UTF-8',  delimiter=',',low_memory=False)
df=pd.DataFrame(data)
df['lat']=pd.to_numeric(df['lat'])
df['lon']=pd.to_numeric(df['lon'])
map=folium.Map(
    location=[df['lat'].mean(),df['lon'].mean()],
    zoom_start=8,
    control_scale=True)
marker_cluster=plugins.MarkerCluster().add_to(map)

loc=[]
for i in range(len(df['lat'])):
    loc.append([df['lat'][i],df['lon'][i]])
folium.PolyLine(loc).add_to(map)

for name,row in df.iterrows():
    iframe=folium.IFrame('<b><h2>{tele}&nbsp;{name}</h2></b{addr}><hr><br>{addr}<br>{tele}'.format(
            name=row['車站中文名稱'],
            addr=row['車站英文名稱'],
            tele=row['車站編號']))
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(iframe,min_width=400, max_width=400),
        tooltip='{name}'.format(name=row['車站中文名稱'])).add_to(marker_cluster)
map.save('alll.html')