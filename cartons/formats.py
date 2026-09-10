from .routing import route
from shapely import LineString
from shapely import to_geojson
def routing(coords: list, transport: str, base_url: str):
    getroute=route(base_url, coords, transport)
    return getroute

def line_string_route(coords: list, transport: str, base_url: str):
    LineStringroute = route(base_url, coords, transport)
    LineStringcoords = LineStringroute.geometry
    linestring = LineString(LineStringcoords)
    return linestring

def geo_json_geometry(coords: list, transport: str, base_url: str):
    linestring = line_string_route(coords, transport, base_url)
    geojsongeometry = to_geojson(linestring)
    return geojsongeometry