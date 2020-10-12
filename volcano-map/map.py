import folium
import pandas as pd


def select_color(e):
    if e < 2000:
        return 'green'
    elif e < 3000:
        return 'orange'
    else:
        return 'red'


# Load the volcanoes data
data = pd.read_csv("Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
name = list(data.NAME)
elev = list(data.ELEV)

# create base map
m = folium.Map(
    location=[41.31256, -118.2669679],
    zoom_start=5,
    width='80%',
    height='80%',
    left='10%',
    top='10%',
    tiles='Stamen Terrain')

# create a feature group
fg = folium.FeatureGroup(name='My Map')

# html for popup
html = """
	<b><a href='https://www.google.com/search?q={}%20volcano' target='_blank'>{}</a></b><br>
	Height: {} m
"""

# add Markers to feature group
for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=5,
        popup=folium.Popup(
            html=html.format(nm, nm, el), max_width=200),
        color=select_color(el),
        fill=True)
    )

# add feature group to base map
m.add_child(fg)


# save as web page
m.save("map1.html")
