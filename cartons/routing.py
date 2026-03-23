from routingpy import OSRM

def route(base_url,coords_lon_lat:[], transport):
    router = OSRM(base_url=base_url)
    coords = coords_lon_lat
    
    route = router.directions(
        overview = "full",
        profile = transport,
        locations = coords
    )
    return route
