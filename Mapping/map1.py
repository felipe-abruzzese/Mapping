import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'blue'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev): #A função zip() permite passar por duas listas em sequência tipo: [a1, a2, a3] e [b1, b2, b3] o resultado será: [a1, b1, a2, b2, a3, b3]
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe),
    fill_color= color_producer(el), color = 'grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) # A função Lambda é uma função que funciona em uma linha só

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
