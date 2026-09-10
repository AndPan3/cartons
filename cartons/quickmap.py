import folium
from .routing import route
from.helpers import Coordinates, _to_folium, _warning_coords

def quick_map(
        base_url,
        coords: Coordinates,
        osrm_profile: str
):
    _warning_coords(coords)
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
