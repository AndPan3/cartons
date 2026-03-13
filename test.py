import cartons
import webbrowser
#Zürich-Geneva
map=cartons.draw("https://router.project-osrm.org",8.5431473,47.3669154,6.1426172,46.2086997,"red","5","OpenStreetMap","car")
filename = "route.html"
map.save(filename)
webbrowser.open(filename)