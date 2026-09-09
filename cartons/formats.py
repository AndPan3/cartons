from .routing import route
import shapely
def routing(coords: list, transport: str, base_url: str):
    getroute=route(base_url, coords, transport)
    return getroute

def LineStringRoute(coords: list, transport: str, base_url: str):
    LineStringroute = route(base_url, coords, transport)
    LineStringcoords = LineStringroute.geometry
    linestring = shapely.geometry.LineString(LineStringcoords)
    return linestring

def GeoJsonGeometry(coords: list, transport: str, base_url: str):
    linestring = LineStringRoute(coords, transport, base_url)
    geojsongeometry = shapely.to_geojson(linestring)
    return geojsongeometry