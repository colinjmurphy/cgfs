from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light


class AmbientLight(Light):
    def illuminate(self, point: Point, normal: Vector) -> float:
        return self._intensity
