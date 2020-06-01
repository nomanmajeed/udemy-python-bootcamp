import folium
import pandas as pd

data = pd.read_csv("volcanos.txt")
lat = list(data.LAT)
lon = list(data.LON)
loc = list(data.LOCATION)
elev = list(data.ELEV)


def color_maker(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[lat[0], lon[0]],
                 tiles='Stamen Terrain',
                 zoom_start=6)


fg = folium.FeatureGroup(name="My Map")
for i, j, k, l in zip(lat, lon, loc, elev):

    fg.add_child(folium.Marker(
        location=[i, j], tooltip=k+" ("+str(l)+"m)", icon=folium.Icon(color=color_maker(l))))


map.add_child(fg)
map.save("map2.html")
