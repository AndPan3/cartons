from cartons import map_route
map_route(
    base_url="http://router.project-osrm.org",
    coords=[(13.388860, 52.517037), (13.397634, 52.529407)],
    osrm_profile="driving",
    color="red",
    weight=5,
    tiles="OpenStreetMap",
    attribution="OpenStreetMap contributors",
)
map_route(
    base_url="http://router.project-osrm.org",
    coords=[(13.388860, 52.517037), (47.349375, 7.907760),(13.397634, 52.529407)],
    osrm_profile="driving",
    color="blue",
    weight=10,
    tiles="CartoDB Dark_Matter",
    attribution="© CartoDB Dark_Matter"
)