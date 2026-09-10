from cartons import geo_json_geometry
from cartons import line_string_route
geo_json_geometry(base_url="http://router.project-osrm.org", coords=[(13.388860, 52.517037), (13.397634, 52.529407)], osrm_profile="driving")
geo_json_geometry(base_url="http://router.project-osrm.org", coords=[(13.388860, 52.517037), (47.349375, 7.907760),(13.397634, 52.529407)], osrm_profile="driving")

line_string_route(base_url="http://router.project-osrm.org", coords=[(13.388860, 52.517037), (13.397634, 52.529407)], osrm_profile="driving")
line_string_route(base_url="http://router.project-osrm.org", coords=[(13.388860, 52.517037), (47.349375, 7.907760),(13.397634, 52.529407)], osrm_profile="driving") 