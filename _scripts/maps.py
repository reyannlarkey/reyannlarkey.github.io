import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
from folium import IFrame

#help(folium.Icon)
# Function for displaying the map
def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='50%', height='200px')

m_1 = folium.Map(location=[38.2727,-153.2813], tiles='openstreetmap', zoom_start=3, min_zoom = 2) # initiallize the map

def ground_unit(Lat, Lon, NAME, DATE, RECOVERED):

    html = """
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;}
        .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
        .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
        .tg .tg-zlqz{font-weight:bold;background-color:#c0c0c0;border-color:inherit;text-align:center;vertical-align:top}
        .tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
        </style>
        <table class="tg">
          <tr>
            <th class="tg-zlqz">Date</th>""" + f'\n\
            <th class="tg-c3ow">{DATE}</th>' + """
          </tr>
          <tr>
            <td class="tg-zlqz">Unit Name</td>""" + f'\n\
            <td class="tg-c3ow">{NAME}</td>' + """
          </tr>
          <tr>
            <td class="tg-zlqz">Recovered</td>""" + f'\n\
            <td class="tg-c3ow">{RECOVERED}</td>' + """
          </tr>
        </table>
        """

    iframe = IFrame(html=html, height=130, width=230)
    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker(location=[Lat, Lon], icon=folium.Icon(icon='fa-bolt', color='blue', prefix='fa'),
                  popup=popup).add_to(m_1)





def flight_unit(flight_file, NAME, DATE, RECOVERED, track_color = 'blue'):
    balloon_launches = pd.read_csv(flight_file)
    balloon_launches['coords'] = list(zip(balloon_launches.Lat, balloon_launches.Lon))

    html = """
    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
    .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
    .tg .tg-zlqz{font-weight:bold;background-color:#c0c0c0;border-color:inherit;text-align:center;vertical-align:top}
    .tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
    </style>
    <table class="tg">
      <tr>
        <th class="tg-zlqz">Date</th>"""+f'\n\
        <th class="tg-c3ow">{DATE}</th>'+"""
      </tr>
      <tr>
        <td class="tg-zlqz">Unit Name</td>"""+f'\n\
        <td class="tg-c3ow">{NAME}</td>'+"""
      </tr>
      <tr>
        <td class="tg-zlqz">Recovered</td>"""+f'\n\
        <td class="tg-c3ow">{RECOVERED}</td>'+"""
      </tr>
    </table>
    """

    iframe = IFrame(html=html, height=130, width=230)
    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker(location=balloon_launches.coords.values[0], icon=folium.Icon(icon='fa-ship', color=track_color, prefix='fa'),popup=popup).add_to(m_1)
    folium.Marker(location=balloon_launches.coords.values[-1], icon=folium.Icon(icon='fa-plane', color='green', prefix='fa')).add_to(m_1)

    folium.PolyLine(locations=balloon_launches.coords, color=track_color).add_to(m_1)

ground_unit(Lat = 36.663504, Lon = 136.649678-360, NAME = "GU1", DATE = "12-16-2018", RECOVERED= "N/A")
ground_unit(Lat = 35.713397, Lon = 139.763085-360, NAME = "GU2", DATE = "01-11-2019", RECOVERED= "N/A")
ground_unit(Lat = 45.676998, Lon =-111.042931,     NAME = "GU3", DATE = "06-27-2019", RECOVERED= "N/A")
ground_unit(Lat = 43.625913, Lon = -79.396027,    NAME = "GU4", DATE = "07-11-2019", RECOVERED= "N/A")
ground_unit(Lat = 38.742222, Lon = -104.864444,    NAME = "GU5", DATE = "07-11-2019", RECOVERED= "N/A")


flight_unit(flight_file='flight0.csv', NAME = "FU1", DATE = "11-12-2018", RECOVERED="TRUE",track_color='blue')
flight_unit(flight_file='flight_palm_tree.csv', NAME = "FU3", DATE = "07-25-2019", RECOVERED="TRUE",track_color='red')
flight_unit(flight_file='FU2_Flight.csv', NAME = "FU2", DATE = "07-26-2019", RECOVERED="FALSE",track_color='purple')
flight_unit(flight_file='flight1.csv', NAME = "FU3", DATE = "08-06-2019", RECOVERED="TRUE",track_color='pink')

m_1.add_child(folium.LatLngPopup())


embed_map(m_1, 'm_2.html')
