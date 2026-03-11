from .routing import get_route
import folium
def draw(base_url, lon1, lat1, lon2, lat2, col, weight):

    route = get_route(base_url, lon1, lat1, lon2, lat2)

    routecoords = route.geometry #shame commit..
    foliumcoords = [[lat, lon] for lon, lat in routecoords]
    m = folium.Map(
    location=(lat1, lon1),
    control_scale=True,
    )
    folium.Polyline(
        foliumcoords, color=col, weight=weight).add_to(m)
    return m