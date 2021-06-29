from abc import ABC, abstractmethod
from typing import Iterator, Tuple

from PIL import Image

from cgfs.cgfs_types import Color


class Canvas(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def put_pixel(self, pixel_index: int, color: Color):
        pass

    @abstractmethod
    def pixel_iterator(self) -> Iterator[Tuple[int, int, int]]:
        pass


class PillowCanvas(Canvas):
    PIXEL_WIDTH = 4

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._half_width = self.width // 2
        self._half_height = (self.height + 1) // 2

        self._byte_array = bytearray(width * height * self.PIXEL_WIDTH)
        self._image = Image.frombuffer('RGBA', (width, height), self._byte_array)

    def put_pixel(self, pixel_index: int, color: Color):
        byte_index = pixel_index * self.PIXEL_WIDTH
        for i in range(self.PIXEL_WIDTH - 1):
            self._byte_array[byte_index + i] = color[i]
        self._byte_array[byte_index + self.PIXEL_WIDTH - 1] = 255

    def pixel_iterator(self) -> Iterator[Tuple[int, int, int]]:
        for i in range(self.width * self.height):
            y, x = divmod(i, self.width)
            yield x - self._half_width, self._half_height - y - 1, i

    def show(self):
        self._image.show()
