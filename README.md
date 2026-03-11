# cartons

A small Python toolkit for **routing and map visualization**.

`cartons` calculates routes using **OSRM** (via `routingpy`) and renders them on an **interactive Leaflet map** using `folium`.

With only a few lines of code you can compute a route between two coordinates and generate an HTML map displaying the route.

The library is designed to be **simple, lightweight, and easy to integrate into scripts or small projects.**

---

## Demo

Live demo:

https://router.project-osrm.org

This public OSRM server is used in the examples to calculate routes.

---

## Features

- Simple interface for route calculation
- Interactive map rendering
- Uses the OSRM routing engine
- Lightweight with minimal dependencies
- Generates shareable HTML maps

---

## Installation

`cartons` is available on **PyPI**.

### Install from PyPI

```bash
pip install cartons
```

### Install from source

```bash
git clone https://github.com/yourname/cartons.git
cd cartons
pip install -e .
```

### Dependencies

- routingpy
- folium

These will be installed automatically when installing the package.

---

## Quick Example

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

Open the generated file in a browser to view the map.

---

## Project Structure

```text
cartons/
├── routing.py
├── display.py
└── __init__.py
```

### routing.py

Handles communication with the **OSRM routing engine** using `routingpy`.

It sends coordinates to the routing server and returns the routing response.

---

### display.py

Responsible for rendering the route on a **Leaflet map** using `folium`.

OSRM returns coordinates in the format:

```text
[lon, lat]
```

Since **Folium expects `[lat, lon]`**, the coordinates are converted before drawing the route.

---

## Public OSRM Server

Examples use the public OSRM demo server:

```
https://router.project-osrm.org
```

This server is suitable for:

- testing
- small scripts
- experimentation

For **production use**, running your own OSRM server is recommended.

---

## API

### draw(base_url, lon1, lat1, lon2, lat2, col="blue", weight=5)

Calculate a route and return a `folium.Map` object.

#### Parameters

| Parameter | Description |
|----------|-------------|
| base_url | OSRM server URL |
| lon1 | Start longitude |
| lat1 | Start latitude |
| lon2 | Destination longitude |
| lat2 | Destination latitude |
| col | Route color |
| weight | Line thickness |

#### Returns

```
folium.Map
```

---

## Goals

`cartons` aims to provide:

- a **simple routing interface**
- **quick map visualization**
- **minimal dependencies**
- easy integration into **Python scripts**

---

## License

MIT License