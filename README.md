# Cartons

[![PyPI version](https://img.shields.io/pypi/v/cartons?label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/cartons/)
[![Python versions](https://img.shields.io/pypi/pyversions/cartons?logo=python&logoColor=white)](https://pypi.org/project/cartons/)
[![License](https://img.shields.io/github/license/AndPan3/cartons)](otherfiles/LICENSE)
[![Cartons CI](https://github.com/AndPan3/cartons/actions/workflows/tests.yml/badge.svg)](https://github.com/AndPan3/cartons/actions/workflows/tests.yml)

A lightweight Python toolkit for **OSRM routing, route geometry conversion, and interactive Folium maps**.

Cartons provides a small API for going from coordinates to routes, maps, Shapely geometry, and GeoJSON without having to wire together OSRM, RoutingPy, Folium, and Shapely yourself.

```text
coordinates
    │
    ├── route() ──────────────> OSRM route
    │
    ├── map_route() ──────────> configurable Folium map
    │
    ├── quick_map() ──────────> quick Folium map
    │
    ├── line_string_route() ──> Shapely LineString
    │
    └── geo_json_geometry() ──> GeoJSON geometry
```

## Preview

### Geneva → Zürich

![Geneva to Zürich route](img/img1.png)

### Bern → Zürich

![Bern to Zürich route](img/img2.png)

### Route detail

![Zoomed route detail](img/img3.png)

## Installation

Cartons requires **Python 3.10 or newer**.

```bash
python -m pip install cartons
```

To install the latest repository version instead:

```bash
python -m pip install "git+https://github.com/AndPan3/cartons.git"
```

## Quick start

```python
import cartons

coords = [
    [7.4442153, 46.94686],    # Bern
    [8.5431302, 47.3668725],  # Zürich
]

result = cartons.route(
    "https://router.project-osrm.org",
    coords,
    "driving",
)

print(result.distance)
print(result.duration)
```

Routing coordinates are supplied as:

```text
[longitude, latitude]
```

Cartons requires at least two coordinates.

## Quick map

If you just want to route some coordinates and display the result:

```python
import cartons

coords = [
    [7.4442153, 46.94686],
    [8.5431302, 47.3668725],
]

m = cartons.quick_map(
    "https://router.project-osrm.org",
    coords,
    "driving",
)

m.save("route.html")
```

`quick_map()` uses a simple predefined map style and automatically fits the map around the returned route.

## Configurable route map

Use `map_route()` when you want control over the map appearance:

```python
import cartons

coords = [
    [7.4442153, 46.94686],
    [8.5431302, 47.3668725],
]

m = cartons.map_route(
    "https://router.project-osrm.org",
    coords,
    color="red",
    weight=5,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron",
    osrm_profile="driving",
    marker=True,
)

m.save("route.html")
```

`map_route()`:

- requests a route from OSRM
- converts the returned `[lon, lat]` geometry to Folium's `[lat, lon]` order
- draws the route as a `PolyLine`
- optionally adds start and end markers
- automatically fits the map around the route
- returns a `folium.Map`

## Draw existing coordinates

`draw()` does **not** calculate a route.

Use it when you already have coordinates that you want to display:

```python
import cartons

coords = [
    [46.94686, 7.4442153],
    [47.3668725, 8.5431302],
]

m = cartons.draw(coords)

m.save("line.html")
```

Because these coordinates are passed directly to Folium, `draw()` expects:

```text
[latitude, longitude]
```

You can customize the map:

```python
m = cartons.draw(
    coords,
    color="purple",
    weight=7,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron",
)
```

## Coordinate order

Cartons uses two coordinate conventions depending on what you are doing.

### Routing

Functions that send coordinates to OSRM use:

```text
[longitude, latitude]
```

This applies to:

```python
cartons.route()
cartons.map_route()
cartons.quick_map()
cartons.line_string_route()
cartons.geo_json_geometry()
```

Example:

```python
coords = [
    [7.4442153, 46.94686],
    [8.5431302, 47.3668725],
]
```

### Direct drawing

`cartons.draw()` uses Folium-ready coordinates:

```text
[latitude, longitude]
```

Example:

```python
coords = [
    [46.94686, 7.4442153],
    [47.3668725, 8.5431302],
]
```

`map_route()` and `quick_map()` handle the OSRM → Folium coordinate conversion internally.

## Public API

Cartons currently exposes six functions from the package root:

| Function | Purpose | Returns |
|---|---|---|
| `route()` | Calculate an OSRM route | RoutingPy route result |
| `map_route()` | Calculate and draw a configurable route | `folium.Map` |
| `quick_map()` | Calculate and quickly draw a route | `folium.Map` |
| `draw()` | Draw existing coordinates without routing | `folium.Map` |
| `line_string_route()` | Calculate a route and convert its geometry | `shapely.LineString` |
| `geo_json_geometry()` | Calculate a route and convert its geometry to GeoJSON | `str` |

All six can be imported directly:

```python
from cartons import (
    route,
    map_route,
    quick_map,
    draw,
    line_string_route,
    geo_json_geometry,
)
```

## `route()`

```python
route(base_url, coords, osrm_profile)
```

Calculates a route using an OSRM-compatible server.

```python
result = cartons.route(
    "https://router.project-osrm.org",
    [
        [6.143158, 46.204391],
        [8.541694, 47.376887],
    ],
    "driving",
)
```

Cartons requests the full route overview from RoutingPy/OSRM.

The returned RoutingPy object can provide data such as:

```python
result.geometry
result.distance
result.duration
```

The geometry uses `[longitude, latitude]` order.

### Multiple waypoints

More than two coordinates can be supplied:

```python
coords = [
    [6.143158, 46.204391],  # Geneva
    [7.447447, 46.948271],  # Bern
    [8.541694, 47.376887],  # Zürich
]

result = cartons.route(
    "https://router.project-osrm.org",
    coords,
    "driving",
)
```

Coordinates are visited in the order supplied.

## `map_route()`

```python
map_route(
    base_url,
    coords,
    color,
    weight,
    tiles,
    attribution,
    osrm_profile,
    marker=True,
)
```

Calculates a route and displays it on a configurable Folium map.

| Parameter | Description |
|---|---|
| `base_url` | OSRM server URL |
| `coords` | Routing coordinates in `[lon, lat]` order |
| `color` | Route line color |
| `weight` | Route line width |
| `tiles` | Folium tile provider or tile URL |
| `attribution` | Attribution for the tile source |
| `osrm_profile` | Profile passed to OSRM |
| `marker` | Whether to add start/end markers; defaults to `True` |

Returns a `folium.Map`.

## `quick_map()`

```python
quick_map(base_url, coords, osrm_profile)
```

A simpler route-to-map helper.

It calculates the route, creates a Folium map, draws the route, fits the map around it, and returns the resulting `folium.Map`.

Use `map_route()` instead when you need custom styling or endpoint markers.

## `draw()`

```python
draw(
    coords,
    color="blue",
    weight=5,
    tiles="CartoDB Positron",
    attribution="© CartoDB Positron",
)
```

Draws an existing path without contacting OSRM.

`coords` must already be in Folium's `[latitude, longitude]` order.

Returns a `folium.Map`.

## `line_string_route()`

```python
line_string_route(coords, osrm_profile, base_url)
```

Calculates an OSRM route and converts the returned geometry to a Shapely `LineString`.

```python
line = cartons.line_string_route(
    [
        [7.4442153, 46.94686],
        [8.5431302, 47.3668725],
    ],
    "driving",
    "https://router.project-osrm.org",
)

print(line)
```

The coordinates remain geographic longitude/latitude coordinates.

> `LineString.length` therefore represents coordinate degrees, not road distance in metres or kilometres. Use the routing result's distance when you need routed distance.

## `geo_json_geometry()`

```python
geo_json_geometry(coords, osrm_profile, base_url)
```

Calculates a route, converts it to a Shapely `LineString`, and serializes that geometry as GeoJSON.

```python
geojson = cartons.geo_json_geometry(
    [
        [7.4442153, 46.94686],
        [8.5431302, 47.3668725],
    ],
    "driving",
    "https://router.project-osrm.org",
)

print(geojson)
```

The return value is a **GeoJSON geometry string**, not a complete GeoJSON `Feature` or `FeatureCollection`.

## OSRM servers

Cartons is a client library. It does **not** contain its own routing engine.

You provide an OSRM-compatible server:

```python
base_url = "https://router.project-osrm.org"
```

The public OSRM demo server is useful for development and experimentation. Applications with production requirements should use an appropriate routing service or their own OSRM deployment.

The meaning and availability of routing profiles depend on the configured OSRM server.

## Map tiles and attribution

Folium maps load map tiles from the configured tile provider.

When choosing custom tiles, make sure you follow the provider's usage and attribution requirements.

Cartons does not host or proxy map tiles.

## Geometry

OSRM route geometry is represented as:

```text
[longitude, latitude]
```

`line_string_route()` preserves that order when constructing the Shapely geometry.

For Folium maps, Cartons internally converts routed geometry to:

```text
[latitude, longitude]
```

because that is the order expected by Folium/Leaflet.

## Errors

All public functions that operate on coordinate sequences require at least two coordinates.

For example:

```python
cartons.route(
    "https://router.project-osrm.org",
    [[7.4442153, 46.94686]],
    "driving",
)
```

raises:

```text
ValueError: At least 2 coordinates are required.
```

Errors from RoutingPy, OSRM, Folium, Shapely, the network, or an invalid server configuration are otherwise allowed to propagate to the caller.

## Testing

Cartons uses automated smoke tests with GitHub Actions.

On pushes and pull requests, CI:

1. checks out the repository
2. sets up Python
3. installs Cartons directly from the checked-out commit
4. verifies the public imports
5. runs routing tests
6. runs `map_route()` tests
7. runs `quick_map()` tests
8. runs `draw()` tests
9. runs geometry-format tests

If any test script exits with an error, the CI job fails.

This keeps the tests intentionally simple: the smoke suite checks that the package installs and its main public functionality executes successfully.

## Development

Clone the repository:

```bash
git clone https://github.com/AndPan3/cartons.git
cd cartons
```

Install the working copy:

```bash
python -m pip install -e .
```

The editable installation lets Python import your local Cartons source while you develop it.

## Dependencies

Cartons builds on:

- [RoutingPy](https://routingpy.readthedocs.io/) for OSRM requests
- [Folium](https://python-visualization.github.io/folium/) for interactive maps
- [Shapely](https://shapely.readthedocs.io/) for geometry and GeoJSON conversion

These dependencies are installed automatically with Cartons.

## Scope

Cartons intentionally stays small.

Its job is primarily:

```text
coordinates → route → geometry/map
```

It is not intended to replace a complete GIS framework, routing server, geocoder, or navigation application.

## Privacy

Routing functions send the coordinates you provide to the configured OSRM server.

Interactive Folium maps may also cause the browser displaying the map to request tiles from the configured tile provider.

Choose routing and tile services appropriate for the sensitivity of your data.

## Contributing

Issues and pull requests are welcome.

When changing public functionality, run the smoke-test scripts before submitting the change. GitHub Actions will also run them automatically after the change is pushed.

## License

Cartons is released under the MIT License. See `otherfiles/LICENSE`.

## AI assistance

The GitHub Actions CI workflow was created with AI assistance.

The Cartons package source code was written by the maintainer.