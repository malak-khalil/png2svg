from PIL import Image


def sample_hexagon_color(
    image: Image.Image,
    center_x: float,
    center_y: float,
    radius: float,
) -> tuple[int, int, int]:
    """Return the average RGB color of pixels inside a hexagon."""
    if radius <= 0:
        raise ValueError("Hexagon radius must be positive")

    if image.mode != "RGB":
        raise ValueError("Image must be in RGB mode")

    red = green = blue = count = 0

    min_x = max(0, int(center_x - radius))
    max_x = min(image.width, int(center_x + radius) + 1)
    min_y = max(0, int(center_y - radius))
    max_y = min(image.height, int(center_y + radius) + 1)

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            dx = abs((x + 0.5) - center_x)
            dy = abs((y + 0.5) - center_y)

            # Pointy-top hexagon: check if pixel is inside.
            if (
                dx <= radius * 0.8660254
                and dy <= radius
                and dy <= radius - dx / 1.7320508
            ):
                pixel = image.getpixel((x, y))
                assert isinstance(pixel, tuple) and len(pixel) == 3

                r, g, b = pixel
                red += r
                green += g
                blue += b
                count += 1

    if count == 0:
        raise ValueError("No image pixels inside the hexagon")

    return (
        round(red / count),
        round(green / count),
        round(blue / count),
    )
