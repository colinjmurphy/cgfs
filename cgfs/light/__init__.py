from abc import abstractmethod

from cgfs.cgfs_types import Point, Vector


class Light:
    def __init__(self, intensity: float):
        self._intensity = intensity

    @abstractmethod
    def illuminate(self, point: Point, normal: Vector) -> float:
        pass
