from math import sqrt
from pathlib import Path

from png2svg.hexagon import generate_hexagon
from png2svg.image import load_image
from png2svg.sampling import sample_hexagon_color


def convert_png_to_svg(
    input_path: str | Path,
    output_path: str | Path,
    radius: float = 5,
) -> None:
    """Convert a PNG image into an SVG wallpaper of colored hexagons."""
    if radius <= 0:
        raise ValueError("Hexagon radius must be positive")

    image = load_image(input_path)
    width, height = image.size

    horizontal_step = sqrt(3) * radius
    vertical_step = 1.5 * radius

    polygons = []

    row = 0
    center_y = 0.0

    while center_y < height + radius:
        center_x = (horizontal_step / 2) if row % 2 else 0.0

        while center_x < width + radius:
            try:
                color = sample_hexagon_color(image, center_x, center_y, radius)
            except ValueError as error:
                if str(error) == "No image pixels inside the hexagon":
                    center_x += horizontal_step
                    continue
                raise

            polygon = generate_hexagon(center_x, center_y, radius, color)
            polygons.append(polygon)

            center_x += horizontal_step

        center_y += vertical_step
        row += 1

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n' + "\n".join(polygons) + "\n</svg>\n"
    )

    Path(output_path).write_text(svg, encoding="utf-8")
