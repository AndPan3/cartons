from routingpy import OSRM

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
