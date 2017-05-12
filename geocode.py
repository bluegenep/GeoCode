import folium
import jinja2
import pandas as pd
from folium import GeoJson


def getVolcanoes():

    df = pd.read_csv("Volcanoes-USA.txt")

    for (lat, log) in zip(df['LAT'],df['LON']):
        print lat,log


    map1 = folium.Map(location=[45.372, -121.697], zoom_start= 12, tiles='Mapbox bright')

    folium.Marker(location=[45.3288, -121.6625],popup="Mt Hood", icon=folium.Icon(color='red')).add_to(map1)
    folium.Marker(location=[50.3, -120.5], popup="Mt Everest", icon=folium.Icon(color='blue')).add_to(map1)


    map1.save("test.html")

def getColor(elev):
    df = pd.read_csv("Volcanoes-USA.txt")
    step = int((df["ELEV"].max() - df["ELEV"].min())/3)
    minVal = int(df["ELEV"].min())
    maxVal = df["ELEV"].max()

    if elev in range(minVal, minVal + step):
        col = "green"
    elif elev in range(minVal + step, minVal+step *2):
        col = "orange"
    else:
        col = "red"
    return  col

def getVagin():
    df = pd.read_csv("Volcanoes-USA.txt")
    map2 = folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start= 6, tiles='Stamen Terrain')


    fg = folium.FeatureGroup(name="Volcano Location")

    for i,j,k,l in zip(df['LAT'], df['LON'], df["NAME"], df["ELEV"]):
        fg.add_child(folium.Marker(location=[i,j], popup =k, icon=folium.Icon(color = getColor(l),icon_color="green")))
        #folium.Marker(location=[i, j],popup=k, icon=folium.Icon(color = getColor(l),icon_color="green")).add_to(map2)

    map2.add_child(fg)
    map2.add_child(folium.GeoJson(data = open("worldpopulation.json"), name = "World Population",
                                  style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else "orange" if 10000000 <x['properties']['POP2005'] <20000000 else 'red'} ))


    #adding layer control
    map2.add_child(folium.LayerControl())

    map2.save(("test.html"))


getVagin()
