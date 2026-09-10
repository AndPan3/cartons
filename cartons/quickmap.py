import folium
from .routing import route
from.helpers import Coordinates, _to_folium

def quick_map(
        base_url,
        coords: Coordinates,
        osrm_profile: str
):
    if len(coords)>2:
        raise ValueError("Atleast 2 coordinates are required.")
    
    getroute=route(base_url,
                    coords,
                    osrm_profile)

    routecoords = getroute.geometry
    foliumcoords = _to_folium(routecoords)
    sm = folium.Map(
        tiles="CartoDB Positron",
        attr="Copyright: CartoDB Positron",
        control_scale=True,

    )

    folium.PolyLine(
        foliumcoords,
        colour="red",
        weight=5
    ).add_to(sm)
    sm.fit_bounds(foliumcoords)
    return sm
