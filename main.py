import argparse

import folium
import webview


def _get_map_with_geojson(geojson_file: str) -> folium.Map:
    """
    Plots a GeoJSON file using Folium and returns the Map Instance
    Args:
        geojson_file (str): Path to the input GeoJSON file.
    """
    m = folium.Map()

    geojson = folium.GeoJson(geojson_file, name="geojson")
    geojson.add_to(m)

    bounds = geojson.get_bounds()
    m.fit_bounds(bounds)

    return m


def main():
    parser = argparse.ArgumentParser(description="GeoJSON Viewer")
    parser.add_argument("--geojson", help="Path to the input GeoJSON File", required=True)
    args = parser.parse_args()

    map = _get_map_with_geojson(args.geojson)

    webview.create_window("geoJSON Viewer", html=map.get_root().render())
    webview.start()


if __name__ == "__main__":
    main()
