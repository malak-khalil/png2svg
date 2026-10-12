import pytest
from PIL import Image

from png2svg.image import load_image


def test_load_png_returns_rgb_image(tmp_path):
    path = tmp_path / "sample.png"
    Image.new("RGBA", (10, 10), (255, 0, 0, 128)).save(path)

    image = load_image(path)

    assert image.size == (10, 10)
    assert image.mode == "RGB"
    assert image.getpixel((0, 0)) == (255, 0, 0)


def test_load_png_missing_file(tmp_path):
    path = tmp_path / "missing.png"

    with pytest.raises(FileNotFoundError):
        load_image(path)
