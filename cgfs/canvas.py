from abc import ABC, abstractmethod

from PIL import Image

from cgfs.cgfs_types import Color


class Canvas(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2

    @abstractmethod
    def put_pixel(self, x: int, y: int, color: Color):
        pass


class PillowCanvas(Canvas):
    PIXEL_WIDTH = 4

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._byte_array = bytearray(width * height * self.PIXEL_WIDTH)
        self._image = Image.frombuffer('RGBA', (width, height), self._byte_array)

    def put_pixel(self, x: int, y: int, color: Color):
        canvas_index = self._array_index(x, y)
        for i in range(self.PIXEL_WIDTH - 1):
            self._byte_array[canvas_index + i] = color[i]
        self._byte_array[canvas_index + self.PIXEL_WIDTH - 1] = 255

    def show(self):
        self._image.show()

    def _array_index(self, x: int, y: int) -> int:
        assert -self.half_width <= x < self.half_width
        assert -self.half_height <= y < self.half_height

        return ((self.half_height - y - 1) * self.width + (self.half_width + x)) * self.PIXEL_WIDTH
