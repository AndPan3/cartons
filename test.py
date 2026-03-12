import cartons
import webbrowser
#Aargau-Zürich
map=cartons.draw("https://router.project-osrm.org",8.21599,47.47906,8.543130,47.3668725,"red",)
filename = "route.html"
map.save(filename)
webbrowser.open(filename)