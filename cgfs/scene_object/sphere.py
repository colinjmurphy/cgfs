from math import inf, sqrt
from typing import Tuple

from cgfs.cgfs_types import Ray, Color, Point
from cgfs.scene_object import SceneObject
from cgfs.utils import sub, dot


class Sphere(SceneObject):
    def __init__(self, center: Point, radius: float, color: Color):
        self._center = center
        self._radius = radius
        self._color = color

    @property
    def color(self) -> Color:
        return self._color

    def intersect(self, ray: Ray) -> Tuple[float, float]:
        d = ray[1]
        co = sub(ray[0], self._center)

        a = dot(d, d)
        b = 2 * dot(co, d)
        c = dot(co, co) - self._radius * self._radius

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return inf, inf
        else:
            sqrt_discriminant = sqrt(discriminant)
            t1 = (-b + sqrt_discriminant) / (2 * a)
            t2 = (-b - sqrt_discriminant) / (2 * a)
            return t1, t2
