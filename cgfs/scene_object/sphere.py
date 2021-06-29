from math import inf, sqrt
from typing import Tuple, Optional

from cgfs.cgfs_types import Ray, Color, Point
from cgfs.scene_object import SceneObject
from cgfs.utils import sub, dot, normalize


class Sphere(SceneObject):
    def __init__(self, location: Point, radius: float, color: Color, specular: Optional[float] = None):
        self._location = location
        self._radius = radius
        self._color = color
        self._specular = specular

    @property
    def color(self) -> Color:
        return self._color

    @property
    def specular(self) -> float:
        return self._specular

    def intersect(self, ray: Ray) -> Tuple[float, float]:
        d = ray[1]
        co = sub(ray[0], self._location)

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

    def normal(self, point: Point):
        return normalize(sub(point, self._location))
