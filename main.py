import argparse

import folium


def plot_geojson(geojson_file: str) -> None:
    """
    Plots a GeoJSON file using Folium and opens it in a Browser.
    Args:
        geojson_file (str): Path to the input GeoJSON file.
    """
    m = folium.Map()

    geojson = folium.GeoJson(geojson_file, name="geojson")
    geojson.add_to(m)

    bounds = geojson.get_bounds()
    m.fit_bounds(bounds)

    m.show_in_browser()


def main():
    parser = argparse.ArgumentParser(description="GeoJSON Viewer")
    parser.add_argument("--geojson", help="Path to the input GeoJSON File", required=True)
    args = parser.parse_args()

    plot_geojson(args.geojson)


if __name__ == "__main__":
    main()
