from .routing import route
from shapely import LineString
from .helpers import Coordinates

from shapely import to_geojson
def routing(coords: Coordinates, osrm_profile: str, base_url: str):
    getroute=route(base_url, coords, osrm_profile)
    return getroute

def line_string_route(coords: Coordinates, osrm_profile: str, base_url: str):
    LineStringroute = route(base_url, coords, osrm_profile)
    LineStringcoords = LineStringroute.geometry
    linestring = LineString(LineStringcoords)
    return linestring

def geo_json_geometry(coords: Coordinates, osrm_profile: str, base_url: str):
    linestring = line_string_route(coords, osrm_profile, base_url)
    geojsongeometry = to_geojson(linestring)
    return geojsongeometry