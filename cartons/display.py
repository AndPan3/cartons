from .routing import get_route
import folium

def draw(base_url, lon1, lat1, lon2, lat2):

    route = get_route(base_url, lon1, lat1, lon2, lat2)

    routecoords = route.routes[0].geometry["coordinates"]
    foliumcoords = [[lat, lon] for lon, lat in routecoords]
    m = folium.Map(
    location=(lat1, lon1),
    control_scale=True,
    )
    folium.Polyline(
        foliumcoords, color='#FF0000', weight=5).add_to(m)
    
    return m
    