from routingpy import OSRM
from shapely.geometry import LineString

def route(base_url,
        coords:list,
        transport):
    router = OSRM(base_url=base_url)
    
    route = router.directions(
        overview = "full",
        profile = transport,
        locations = coords
    )
    return route

def GeoJson(base_url, coords:list, transport):
    geojsonroute = route(base_url, coords, transport)
    geojsoncoords = geojsonroute.geometry
    geojson = LineString(geojsoncoords).__geo_interface__
    return geojson

    