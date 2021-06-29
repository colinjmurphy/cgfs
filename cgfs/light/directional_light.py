from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light
from cgfs.utils import dot, normalize


class DirectionalLight(Light):
    def __init__(self, direction: Point, intensity: float):
        super().__init__(intensity)
        self._direction = normalize(direction)

    def illuminate(self, point: Point, normal: Vector) -> float:
        n_dot_l = dot(normal, self._direction)
        return self._intensity * n_dot_l
