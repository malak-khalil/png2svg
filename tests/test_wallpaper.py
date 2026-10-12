import xml.etree.ElementTree as ET

from PIL import Image

from png2svg.wallpaper import convert_png_to_svg


def test_conversion_creates_svg_file(tmp_path):
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "wallpaper.svg"

    Image.new("RGB", (40, 40), (255, 0, 0)).save(input_path)

    convert_png_to_svg(input_path, output_path, radius=5)

    assert output_path.exists()

    tree = ET.parse(output_path)
    root = tree.getroot()

    assert root.tag.endswith("svg")
    assert root.attrib["width"] == "40"
    assert root.attrib["height"] == "40"


def test_conversion_generates_multiple_hexagons(tmp_path):
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "wallpaper.svg"

    Image.new("RGB", (40, 40), (0, 255, 0)).save(input_path)

    convert_png_to_svg(input_path, output_path, radius=5)

    tree = ET.parse(output_path)
    root = tree.getroot()

    polygons = root.findall(".//{*}polygon")

    assert len(polygons) > 1


def test_conversion_uses_image_colors(tmp_path):
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "wallpaper.svg"

    Image.new("RGB", (40, 40), (255, 0, 0)).save(input_path)

    convert_png_to_svg(input_path, output_path, radius=5)

    tree = ET.parse(output_path)
    root = tree.getroot()

    polygons = root.findall(".//{*}polygon")

    assert len(polygons) > 0
    assert all(
        polygon.attrib["fill"].lower() in ("#ff0000", "rgb(255,0,0)")
        for polygon in polygons
    )
