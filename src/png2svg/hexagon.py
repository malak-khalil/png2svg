import math


def generate_hexagon(
    x: float,
    y: float,
    radius: float,
    color: tuple[int, int, int],
) -> str:
    """Generate an SVG polygon representing a regular hexagon."""
    points = []

    for i in range(6):
        angle = math.radians(60 * i)
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)
        points.append(f"{px:.2f},{py:.2f}")

    vertices = " ".join(points)
    r, g, b = color

    return f'<polygon points="{vertices}" fill="rgb({r},{g},{b})"/>'
