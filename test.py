import cartons
#Bern-Zürich
map=cartons.draw("https://router.project-osrm.org",7.4442153,46.94686,8.5431302,47.3668725,"red",5)
map.save(map.html)