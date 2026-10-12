from png2svg.hexagon import generate_hexagon


def test_hexagon_generates_svg_polygon():
    result = generate_hexagon(50, 50, 10, (255, 0, 0))

    assert result.startswith("<polygon ")
    assert result.endswith("/>")
    assert 'fill="rgb(255,0,0)"' in result


def test_hexagon_has_six_vertices():
    result = generate_hexagon(50, 50, 10, (255, 0, 0))

    points = result.split('points="')[1].split('"')[0].split()

    assert len(points) == 6
