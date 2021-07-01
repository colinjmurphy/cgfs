from math import radians, tan
from typing import Iterable, Tuple

from cgfs.canvas import Canvas
from cgfs.cgfs_types import Point, Ray, Color


class Camera:
    def __init__(self, canvas: Canvas, position: Point, fov: float):
        self._canvas = canvas
        self._position = position
        self._viewport_half_width = .5
        self._viewport_half_height = .25
        self._viewport_half_width = tan(radians(fov / 2))
        self._viewport_half_height = self._viewport_half_width * (self._canvas.height / self._canvas.width)

    def ray_iterator(self) -> Iterable[Tuple[int, Ray]]:
        for i in range(self._canvas.height * self._canvas.width):
            cy, cx = divmod(i, self._canvas.width)
            vx, vy = cx / self._canvas.width, cy / self._canvas.height

            yield i, (self._position, (vx * self._viewport_half_width * 2 - self._viewport_half_width,
                                       -vy * self._viewport_half_height * 2 + self._viewport_half_height,
                                       1))

    def record_ray_color(self, ray_index: int, color: Color):
        self._canvas.put_pixel(ray_index, color)
