from routingpy import OSRM
from shapely.geometry import LineString
from .helpers import Coordinates

def route(base_url,
        coords: Coordinates,
        osrm_profile: str):
    router = OSRM(base_url=base_url)
    
    route = router.directions(
        overview = "full",
        profile = osrm_profile,
        locations = coords
    )
    return route