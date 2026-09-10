from .routing import route
import folium
from .helpers import Coordinates, _to_folium, _markers
def map_route(base_url, 
         coords: Coordinates, 
         color:str, weight:int,
         tiles:str,attribution:str,
         osrm_profile: str,
         marker: bool= True):
    
    if len(coords)>2:
        raise ValueError("Atleast 2 coordinates are required.")
    
    getroute=route(base_url, coords, osrm_profile)
    routecoords = getroute.geometry
    foliumcoords = _to_folium(routecoords) 
    #create_map
    m = folium.Map(
        tiles=tiles,
        attr=attribution,
        control_scale=True,
    )
    _markers(marker, foliumcoords, m)
    
    folium.PolyLine(
        foliumcoords,
        color=color,
        weight=weight
    ).add_to(m)
    m.fit_bounds(foliumcoords)
    return m

def draw(coords: Coordinates, color="blue", weight=5,tiles="CartoDB Positron",attribution="© CartoDB Positron"):
    if len(coords)>2:
        raise ValueError("Atleast 2 coordinates are required.")
    mc = folium.Map(
        zoom_start=2,
        tiles=tiles,
        attr=attribution,
        control_scale=True,
    )

    folium.PolyLine(
        coords,
        color=color,
        weight=weight
    ).add_to(mc)
    mc.fit_bounds(coords)

    return mc
