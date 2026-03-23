from routingpy import OSRM

def route(base_url,
        coords_lon_lat:list,
        transport):
    router = OSRM(base_url=base_url)
    
    route = router.directions(
        overview = "full",
        profile = transport,
        locations = coords_lon_lat
    )
    return route
