from cgfs.types import Color


class Canvas:
    PIXEL_WIDTH = 3

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2
        self._byte_array = bytearray(width * height * self.PIXEL_WIDTH)

    def put_pixel(self, x: int, y: int, color: Color):
        canvas_index = self._array_index(x, y)
        for i in range(self.PIXEL_WIDTH):
            self._byte_array[canvas_index + i] = color[i]

    def _array_index(self, x: int, y: int) -> int:
        assert -self.half_width <= x <= self.half_width
        assert -self.half_height <= y <= self.half_height

        return ((self.half_height - y) * self.width + (self.half_width + x)) * self.PIXEL_WIDTH
