from .routing import get_route
import folium

def draw(base_url, lon1, lat1, lon2, lat2, col="blue", weight=5,tiles="OpenStreetMap", transport="car"):
    route = get_route(base_url, lon1, lat1, lon2, lat2)

    routecoords = route.geometry
    foliumcoords = [[lat, lon] for lon, lat in routecoords]

    m = folium.Map(
        location=(lat1, lon1),
        tiles=tiles,
        control_scale=True,
    )

    folium.PolyLine(
        foliumcoords,
        color=col,
        weight=weight
    ).add_to(m)

    return m