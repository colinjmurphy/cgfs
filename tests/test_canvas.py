from cgfs.canvas import PillowCanvas


def test_coords():
    canvas = PillowCanvas(3, 3)
    assert canvas._byte_array == bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ])

    canvas.put_pixel(0, 0, (1, 2, 3))
    assert canvas._byte_array == bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03, 0xff, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ])

    canvas.put_pixel(-1, 1, (4, 5, 6))
    assert canvas._byte_array == bytearray([
        0x04, 0x05, 0x06, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03, 0xff, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ])


def test_array_index():
    canvas = PillowCanvas(50, 50)
    assert canvas._array_index(-25, 24) == 0
    assert canvas._array_index(24, 24) == 49 * canvas.PIXEL_WIDTH
    assert canvas._array_index(-25, -25) == 50 * 49 * canvas.PIXEL_WIDTH
    assert canvas._array_index(24, -25) == 50 * 50 * canvas.PIXEL_WIDTH - canvas.PIXEL_WIDTH

    expected = 0
    for y in range(24, -25 - 1, -1):
        for x in range(-25, 25):
            assert canvas._array_index(x, y) == expected
            expected += 4

    canvas = PillowCanvas(51, 51)
    assert canvas._array_index(-25, 25) == 0
    assert canvas._array_index(25, 25) == 50 * canvas.PIXEL_WIDTH
    assert canvas._array_index(-25, -25) == 51 * 50 * canvas.PIXEL_WIDTH
    assert canvas._array_index(25, -25) == 50 * 50 * canvas.PIXEL_WIDTH - canvas.PIXEL_WIDTH

    expected = 0
    for y in range(24, -25 - 1, -1):
        for x in range(-25, 25):
            assert canvas._array_index(x, y) == expected
            expected += 4
