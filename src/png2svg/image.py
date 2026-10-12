from pathlib import Path

from PIL import Image


def load_image(path: str | Path) -> Image.Image:
    """Load an image and convert it to RGB mode."""
    with Image.open(path) as image:
        return image.convert("RGB")
