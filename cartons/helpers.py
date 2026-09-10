import folium
from collections.abc import Sequence
def _to_folium(coords):
    return [[lat, lon] for lon, lat in coords]

def _markers(marker: bool, foliumcoords, m):
    if marker:
         folium.Marker(
             location = foliumcoords[0]
         ).add_to(m)
         folium.Marker(
             location = foliumcoords[-1]
         ).add_to(m)

def _warning_coords(coords):
    if len(coords)<2:
        raise ValueError("At least 2 coordinates are required.")
Coordinate = Sequence[float]
Coordinates = Sequence[Coordinate]