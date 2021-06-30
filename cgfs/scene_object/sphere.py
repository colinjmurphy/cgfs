from math import inf, sqrt
from typing import Optional, Iterable

from cgfs.cgfs_types import Ray, Color, Point
from cgfs.scene_object import SceneObject
from cgfs.utils import sub, dot, normalize


class Sphere(SceneObject):
    def __init__(self, location: Point, radius: float, color: Color, specular: Optional[float] = None,
                 reflective: float = 0):
        super().__init__(color, specular, reflective)
        self._location = location
        self._radius = radius

    def intersect(self, ray: Ray, t_min: float = -inf, t_max: float = inf) -> Iterable[float]:
        d = ray[1]
        co = sub(ray[0], self._location)

        a = dot(d, d)
        b = 2 * dot(co, d)
        c = dot(co, co) - self._radius * self._radius

        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            sqrt_discriminant = sqrt(discriminant)
            t1 = (-b + sqrt_discriminant) / (2 * a)
            if t_min <= t1 <= t_max:
                yield t1
            t2 = (-b - sqrt_discriminant) / (2 * a)
            if t_min <= t2 <= t_max:
                yield t2

    def normal(self, point: Point):
        return normalize(sub(point, self._location))
