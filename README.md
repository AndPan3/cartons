
# cartons
[![PyPI version](https://img.shields.io/pypi/v/cartons.svg)](https://pypi.org/project/cartons/)
[![License](https://img.shields.io/github/license/AndPan3/cartons)](https://github.com/AndPan3/cartons/blob/main/LICENSE)
![Downloads](https://img.shields.io/pypi/dm/cartons?style=flat)

**cartons** is a lightweight Python toolkit for **routing** and **interactive map visualization**.

It combines the power of **OSRM** (Open Source Routing Machine) for route calculation with **Folium** for rendering beautiful interactive maps in HTML. With only a few lines of Python, you can calculate a route between two coordinates, extract route data such as geometry, distance, and duration, and display the result on a slippy map.

---

## Why cartons?

`cartons` is made for people who want to work with routes **without building everything from scratch**.

It gives you a clean and simple way to:

- calculate a route between two coordinates
- retrieve the full route object from OSRM
- draw the route on an interactive map
- save the map as an HTML file
- customize route color, line thickness, tiles, and attribution
- work with precomputed coordinate lists for fast visualization

It is intentionally lightweight, easy to understand, and easy to integrate into scripts, notebooks, demos, and small GIS projects.

---

## Preview

### Geneva → Zürich
A long-distance route rendered across Switzerland.

![Geneva to Zürich route](img/img1.png)

### Bern → Zürich
A shorter intercity route, useful for quick demos and examples.

![Bern to Zürich route](img/img2.png)

### Zoomed-in route detail
A close-up example showing that the route geometry stays clear and useful even at high zoom levels.

![Zoomed-in route detail](img/img3.png)

---

## Features

### Routing
- Route calculation between two geographic coordinates
- Uses an OSRM routing server through `routingpy`
- Returns the **full route object**, not just a line
- Route object can expose useful data such as:
  - geometry
  - distance
  - duration

### Visualization
- Draw routes on interactive Folium maps
- Save maps as `.html`
- Open generated maps in a browser
- Zoom and pan freely
- Use custom tile providers
- Use custom route color and line weight

### Lightweight API
- Small, simple public API
- Minimal setup
- Easy to learn
- Good for scripts, prototypes, notebooks, and teaching

### Fast drawing mode
- Draw an already existing coordinate list directly
- Useful when you already have route geometry and do not need to query OSRM again

---

## Installation

Install from PyPI:

```bash
pip install cartons
````

---

## Dependencies

`cartons` is built on top of:

* [routingpy](https://github.com/gis-ops/routingpy) for OSRM access
* [Folium](https://python-visualization.github.io/folium/) for interactive maps

---

## Quick Start

```python
import cartons
import webbrowser

# Bern → Zürich
m = cartons.draw(
    "https://router.project-osrm.org",
    7.4442153, 46.94686,
    8.5431302, 47.3668725,
    col="red",
    weight=5,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron",
    transport="car"
)

filename = "route.html"
m.save(filename)
webbrowser.open(filename)
```

This creates an interactive HTML map with the calculated route drawn on top.

---

## How cartons works

The workflow is simple:

```text
Coordinates
    ↓
cartons.get_route()
    ↓
OSRM route calculation
    ↓
route object returned
    ↓
cartons.draw()
    ↓
Folium map
    ↓
Interactive HTML output
```

---

## Public API

The package exposes these functions:

* `cartons.get_route(...)`
* `cartons.draw(...)`
* `cartons.fastdraw(...)`

These are imported in the package root, so they are available directly after `import cartons`. 

---

## API Reference

## `get_route()`

Calculates a route using an OSRM server and returns the full route object.

```python
cartons.get_route(base_url, lon1, lat1, lon2, lat2, transport="car")
```

### Parameters

| Parameter   | Description                                       |
| ----------- | ------------------------------------------------- |
| `base_url`  | URL of the OSRM routing server                    |
| `lon1`      | Longitude of the start point                      |
| `lat1`      | Latitude of the start point                       |
| `lon2`      | Longitude of the destination                      |
| `lat2`      | Latitude of the destination                       |
| `transport` | Routing profile, such as `car`, `bike`, or `foot` |

### Returns

A route object returned by `routingpy` / OSRM.

### What you can read from the returned route

Typical useful properties include:

* `route.geometry`
* `route.distance`
* `route.duration`

### Example

```python
import cartons

route = cartons.get_route(
    "https://router.project-osrm.org",
    7.4442153, 46.94686,
    8.5431302, 47.3668725,
    transport="car"
)

print("Distance (m):", route.distance)
print("Duration (s):", route.duration)
print("Number of geometry points:", len(route.geometry))
```

### Friendly formatting example

```python
print(f"Distance: {route.distance / 1000:.2f} km")
print(f"Duration: {route.duration / 60:.1f} min")
```

---

## `draw()`

Calculates a route and immediately draws it on a Folium map.

```python
cartons.draw(
    base_url,
    lon1,
    lat1,
    lon2,
    lat2,
    col="blue",
    weight=5,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron",
    transport="car"
)
```

### Parameters

| Parameter     | Description                            |
| ------------- | -------------------------------------- |
| `base_url`    | URL of the OSRM routing server         |
| `lon1`        | Longitude of the start point           |
| `lat1`        | Latitude of the start point            |
| `lon2`        | Longitude of the destination           |
| `lat2`        | Latitude of the destination            |
| `col`         | Route line color                       |
| `weight`      | Route line thickness                   |
| `tiles`       | Tile source used by Folium             |
| `attribution` | Attribution text for the tile provider |
| `transport`   | Routing profile used by OSRM           |

### Returns

A `folium.Map` object.

### What it does internally

* calls `get_route(...)`
* reads `route.geometry`
* converts OSRM coordinate order into Folium coordinate order
* draws the route as a `folium.PolyLine`
* returns the map object

---

## `fastdraw()`

Draws a route directly from an existing list of coordinates. The pre-existing coordinates should be formatted like this:```python [lat,lon],[lat,lon],[lat,lon]```and so on. 


```python
cartons.fastdraw(
    coordslatlon,
    col="blue",
    weight=5,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron"
)
```

### Parameters

| Parameter      | Description                                |
| -------------- | ------------------------------------------ |
| `coordslatlon` | List of coordinates in `[lat, lon]` format |
| `col`          | Route line color                           |
| `weight`       | Route line thickness                       |
| `tiles`        | Tile source used by Folium                 |
| `attribution`  | Attribution text for the tile provider     |

### Returns

A `folium.Map` object.

### When to use `fastdraw()`

Use `fastdraw()` when:

* you already have route coordinates
* you want to visualize custom paths
* you do not want to call the routing server again
* you are drawing preprocessed or cached geometry

---

## Examples

## 1. Calculate a route and inspect metadata

```python
import cartons

route = cartons.get_route(
    "https://router.project-osrm.org",
    6.143158, 46.204391,   # Geneva
    8.541694, 47.376887,   # Zürich
    transport="car"
)

print(f"Distance: {route.distance / 1000:.2f} km")
print(f"Duration: {route.duration / 3600:.2f} h")
```

---

## 2. Draw a route on an interactive map

```python
import cartons

m = cartons.draw(
    "https://router.project-osrm.org",
    6.143158, 46.204391,   # Geneva
    8.541694, 47.376887,   # Zürich
    col="red",
    weight=6,
    transport="car"
)

m.save("geneva_zurich.html")
```

---

## 3. Draw precomputed coordinates

```python
import cartons

coords = [
    [46.94686, 7.4442153],
    [47.0, 7.7],
    [47.15, 8.0],
    [47.3668725, 8.5431302]
]

m = cartons.fastdraw(coords, col="red", weight=5)
m.save("custom_route.html")
```

---

## Use Cases

`cartons` is useful for:

* route visualization
* travel maps
* mobility demos
* logistics prototypes
* educational GIS examples
* interactive notebook demonstrations
* displaying routes in small web or data projects
* working with route geometry in Python

---

## Design Goals

This project is designed to be:

* simple
* readable
* practical
* lightweight
* easy to integrate
* easy to extend

Instead of being a huge GIS framework, `cartons` focuses on doing a small number of routing and visualization tasks well.

---

## Project Structure

```text
cartons/
├── __init__.py
├── routing.py
└── display.py
```

### `routing.py`

Handles route calculation through OSRM.

### `display.py`

Handles map creation and route drawing through Folium.

### `__init__.py`

Exports the public API.

---

## Development

Clone the repository:

```bash
git clone https://github.com/AndPan3/cartons.git
cd cartons
```

Install in editable mode:

```bash
pip install -e .
```

---

## Notes

* `cartons` depends on access to an OSRM server
* the public demo server is great for testing, but production use may require your own server
* returned route data depends on the routing backend and profile used
* `draw()` is best when you want a full route calculation and visualization in one step
* `fastdraw()` is best when you already have coordinates

---

## Roadmap Ideas

Possible future improvements:

* markers for start and end points
* multiple waypoints
* turn-by-turn instructions
* optional automatic map fitting to route bounds
* popup summaries with distance and duration
* GeoJSON export
* route alternatives
* batch route generation

---

## Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or want to improve the project:

1. Open an issue
2. Submit a pull request

---

## License

MIT License

---

## Author

**AndPan3**

---

## Acknowledgements

This project uses:

* **OSRM** for route computation
* **routingpy** as the Python routing interface
* **Folium** for map rendering
* **CartoDB Positron** / compatible tile providers for basemaps
