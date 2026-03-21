import folium
from .routing import route

def simpleroute(
        base_url,
        lon1,lat1,
        lon2,lat2,
        transport
):
    route=route(base_url,
                    lon1,lat1,
                    lon2,lat2,
                    transport)

    routecoords = route.geometry
    fastroutecoords = [[lat, lon] for lon, lat in routecoords]

    sm = folium.Map(
        tiles="CartoDB Positron",
        attr="Copyright: CartoDB Positron",
        control_scale=True,

    )

    folium.PolyLine(
        fastroutecoords,
        color="red",
        weight=5
    ).add_to(sm)
    sm.fit_bounds(fastroutecoords)
    return sm