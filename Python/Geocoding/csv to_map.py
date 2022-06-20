import pandas as pd
import folium
from folium import plugins

data = pd.read_csv('台灣快篩.csv', encoding='UTF-8',  delimiter=',')
park_map = folium.Map(
    location=[data['Lat'].mean(), data['Long'].mean()],
    zoom_start=10,
    control_scale=True)
marker_cluster = plugins.MarkerCluster().add_to(park_map)

for name,row in data.iterrows():
    iframe=folium.IFrame('<b><h2>{name}</h2></b><hr><br>{addr}<br>{tele}'.format(
            name=row['診所名稱'],
            addr=row['診所地址'],
            tele=row['診所電話']),)
    folium.Marker(
        location=[row["Lat"], row["Long"]],
        popup=folium.Popup(iframe,min_width=300, max_width=300),tooltip='{name}'.format(name=row['診所名稱'])).add_to(marker_cluster)
park_map.save('Taiwan COVID-19 rapid antigen test map.html')