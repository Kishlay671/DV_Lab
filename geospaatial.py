import folium
import geopandas as gpd
from IPython.display import display 

# Bhilai coordinates
latitude = 21.1938
longitude = 81.3509

# Create a folium map centered on Bhilai
m = folium.Map(location=[latitude, longitude], zoom_start=12)

# Add a marker for Bhilai
folium.Marker(
    location=[latitude, longitude],
    popup="Bhilai, Chhattisgarh",
    tooltip="Bhilai",
    icon=folium.Icon(color='blue')
).add_to(m)

# Display in Jupyter
display(m)