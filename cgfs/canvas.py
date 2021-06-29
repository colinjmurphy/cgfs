from abc import ABC, abstractmethod
from typing import Iterator, Tuple

from PIL import Image

from cgfs.cgfs_types import Color


class Canvas(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._pixel_count = width * height

    @abstractmethod
    def put_pixel(self, pixel_index: int, color: Color):
        pass

    @abstractmethod
    def pixel_iterator(self) -> Iterator[Tuple[int, int, int]]:
        pass


class ByteArrayCanvas(Canvas):
    COLOR_WIDTH = 3
    PIXEL_WIDTH = 3

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._half_width = self.width // 2
        self._half_height = (self.height + 1) // 2
        self._byte_array = bytearray(self._pixel_count * self.PIXEL_WIDTH)

    def put_pixel(self, pixel_index: int, color: Color):
        byte_index = pixel_index * self.PIXEL_WIDTH
        for i in range(self.COLOR_WIDTH):
            self._byte_array[byte_index + i] = color[i]

    def pixel_iterator(self) -> Iterator[Tuple[int, int, int]]:
        for i in range(self._pixel_count):
            y, x = divmod(i, self.width)
            yield x - self._half_width, self._half_height - y - 1, i


class PillowCanvas(ByteArrayCanvas):
    PIXEL_WIDTH = 4

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._image = Image.frombuffer('RGBX', (width, height), self._byte_array)

    def show(self):
        self._image.show()
