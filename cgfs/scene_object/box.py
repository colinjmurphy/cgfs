from math import inf
from typing import Iterable

from cgfs.cgfs_types import Point, Vector, Ray, Color
from cgfs.scene_object import SceneObject


class Box(SceneObject):
    def __init__(self, corner_a: Point, corner_b: Point, color: Color, specular: float):
        super().__init__(color, specular)
        self._corner_a = corner_a
        self._corner_b = corner_b

    def intersect(self, ray: Ray, t_min: float = -inf, t_max: float = inf) -> Iterable[float]:
        pass

    def normal(self, point: Point) -> Vector:
        pass
