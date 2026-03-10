# cartons

A small Python toolkit for routing and map visualization.

`cartons` calculates routes using **OSRM** (via `routingpy`) and draws them on an interactive **Leaflet map** using `folium`.

With just a few lines of code you can compute a route between two coordinates and render it as an HTML map.

It is designed to be simple, lightweight, and easy to integrate into scripts or small projects.

---

# Installation

Install from PyPI:

```bash
pip install cartons
```

Or install locally from the repository:

```bash
pip install -e .
```

Dependencies:

- routingpy
- folium

---

# Quick Example

```python
import cartons

m = cartons.draw(
    "https://router.project-osrm.org",
    8.5417, 47.3769,
    8.55, 47.38
)

m.save("route.html")
```

This generates an **interactive HTML map** showing the calculated route.

---

# How It Works

The package has two main modules:

```
cartons/
├ routing.py
├ display.py
└ __init__.py
```

### routing.py

Handles communication with the OSRM routing engine using `routingpy`.

It sends coordinates to the routing server and returns the full route response.

### display.py

Extracts route geometry and draws the route using `folium`.

Coordinates returned by OSRM are converted from:

```
[lon, lat]
```

to

```
[lat, lon]
```

because Folium expects latitude first.

---

# Public OSRM Server

The examples use the public demo server:

```
https://router.project-osrm.org
```

This server is suitable for testing and small scripts.

For production usage, running your own OSRM server is recommended.

---

# Project Goals

`cartons` aims to provide:

- simple routing interface
- quick map visualization
- minimal dependencies
- easy integration into Python scripts

---

# License

MIT License
