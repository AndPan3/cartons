from .routing import route
import folium
def draw(base_url, 
         lon1, lat1, 
         lon2, lat2, 
         col="blue", weight=5,
         tiles="CartoDB Positron",attribution="© CartoDB Positron",
         transport: str = "car",
         marker=True):
    getroute=route(base_url, lon1, lat1, lon2, lat2, transport)

    routecoords = getroute.geometry
    foliumcoords = [[lat, lon] for lon, lat in routecoords]

    m = folium.Map(
        tiles=tiles,
        attr=attribution,
        control_scale=True,

    )
    if marker==True:
        folium.Marker([lat1, lon1]).add_to(m)
        folium.Marker([lat2, lon2]).add_to(m)

    folium.PolyLine(
        foliumcoords,
        color=col,
        weight=weight
    ).add_to(m)
    m.fit_bounds(foliumcoords)
    return m

def simpledraw(coordslatlon, col="blue", weight=5,tiles="CartoDB Positron",attribution="© CartoDB Positron"):

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
