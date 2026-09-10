from .routing import route
import folium
def draw(base_url, 
         coords: list, 
         col:str, weight:str,
         tiles:str,attribution:str,
         transport: str,
         marker=True):
    getroute=route(base_url, coords, transport)
    
    routecoords = getroute.geometry
    foliumcoords = [[lat, lon] for lon, lat in routecoords]
    #create_map
    m = folium.Map(
        tiles=tiles,
        attr=attribution,
        control_scale=True,

    )
    #markers
    if marker == True:
         folium.Marker(
             location = foliumcoords[0]
         ).add_to(m)
         folium.Marker(
             location = foliumcoords[-1]
         ).add_to(m)
         
    folium.PolyLine(
        foliumcoords,
        color=col,
        weight=weight
    ).add_to(m)
    m.fit_bounds(foliumcoords)
    return m

def simpledraw(coords: list, col="blue", weight=5,tiles="CartoDB Positron",attribution="© CartoDB Positron"):

    mc = folium.Map(
        zoom_start=2,
        tiles=tiles,
        attr=attribution,
        control_scale=True,
    )

    folium.PolyLine(
        coords,
        color=col,
        weight=weight
    ).add_to(mc)
    mc.fit_bounds(coords)

    return mc
