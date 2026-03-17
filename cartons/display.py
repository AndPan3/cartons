from .routing import get_route
import folium
def draw(base_url, lon1, lat1, lon2, lat2, col="blue", weight=5,tiles="CartoDB Positron",attribution="© CartoDB Positron",transport=""):
    route = get_route(base_url, lon1, lat1, lon2, lat2, transport)

    routecoords = route.geometry
    foliumcoords = [[lat, lon] for lon, lat in routecoords]

    m = folium.Map(
        tiles=tiles,
        attr=attribution,
        control_scale=True,
    )

    folium.PolyLine(
        foliumcoords,
        color=col,
        weight=weight
    ).add_to(m)
    m.fit_bounds(foliumcoords)
    return m

def fastdraw(coordslatlon, col="blue", weight=5,tiles="CartoDB Positron",attribution="© CartoDB Positron"):

    mc = folium.Map(
        zoom_start=2,
        tiles=tiles,
        attr=attribution,
        control_scale=True,
    )
    
    folium.PolyLine(
        coordslatlon,
        color=col,
        weight=weight
    ).add_to(mc)
    mc.fit_bounds(coordslatlon)

    return mc
