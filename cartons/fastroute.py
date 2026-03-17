import folium
from .routing import get_route

def fastroute(
        base_url,
        lon1,lat1,
        lon2,lat2,
        transport
):
    route=get_route(base_url,
                    lon1,lat1,
                    lon2,lat2,
                    transport)

    routecoords = route.geometry
    fastroutecoords = [[lat, lon] for lon, lat in routecoords]

    m = folium.Map(
        tiles="CartoDB Positron",
        attr="Copyright: CartoDB Positron",
        control_scale=True,

    )

    folium.PolyLine(
        fastroutecoords,
        color="red",
        weight=5
    ).add_to(m)
    m.fit_bounds(fastroutecoords)
    return m