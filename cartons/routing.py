from routingpy import OSRM

def get_route(base_url, lon1, lat1, lon2,lat2, transport="car""foot""bike"):
    router = OSRM(base_url=base_url)
    coords = [
        (lon1, lat1),
        (lon2, lat2)]
    
    route = router.directions(
        overview = "full",
        profile = transport,
        locations = coords,
    )
    return route