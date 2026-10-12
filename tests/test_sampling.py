from PIL import Image

from png2svg.sampling import sample_hexagon_color


def test_uniform_image_returns_same_color():
    image = Image.new("RGB", (30, 30), (255, 0, 0))

    result = sample_hexagon_color(image, 15, 15, 8)

    assert result == (255, 0, 0)


def test_mixed_colors_are_averaged():
    image = Image.new("RGB", (30, 30), (0, 0, 0))

    # Left half is red; right half is blue.
    for y in range(30):
        for x in range(15):
            image.putpixel((x, y), (255, 0, 0))
        for x in range(15, 30):
            image.putpixel((x, y), (0, 0, 255))

    result = sample_hexagon_color(image, 14.5, 15, 8)

    assert abs(result[0] - 127) <= 15
    assert result[1] == 0
    assert abs(result[2] - 127) <= 15


def test_hexagon_near_image_boundary():
    image = Image.new("RGB", (20, 20), (0, 255, 0))

    result = sample_hexagon_color(image, 0, 0, 8)

    assert result == (0, 255, 0)
