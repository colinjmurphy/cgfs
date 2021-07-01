from abc import ABC, abstractmethod

from PIL import Image

from cgfs.cgfs_types import Color


class Canvas(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def put_pixel(self, pixel_index: int, color: Color):
        pass


class ByteArrayCanvas(Canvas):
    COLOR_WIDTH = 3
    PIXEL_WIDTH = 3

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._byte_array = bytearray(self.width * self.height * self.PIXEL_WIDTH)

    def put_pixel(self, pixel_index: int, color: Color):
        byte_index = pixel_index * self.PIXEL_WIDTH
        for i in range(self.COLOR_WIDTH):
            self._byte_array[byte_index + i] = color[i]


class PillowCanvas(ByteArrayCanvas):
    PIXEL_WIDTH = 4

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._image = Image.frombuffer('RGBX', (width, height), self._byte_array)

    def show(self):
        self._image.show()
