from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light
from cgfs.utils import dot, sub, length


class PointLight(Light):
    def __init__(self, location: Point, intensity: float):
        super().__init__(intensity)
        self._location = location

    def illuminate(self, point: Point, normal: Vector) -> float:
        l = sub(self._location, point)
        n_dot_l = dot(normal, l)
        return self._intensity * n_dot_l / length(l)
