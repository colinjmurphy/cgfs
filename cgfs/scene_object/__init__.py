from abc import ABC, abstractmethod
from typing import Tuple

from cgfs.cgfs_types import Color, Ray, Point, Vector


class SceneObject(ABC):
    @property
    @abstractmethod
    def color(self) -> Color:
        pass

    @abstractmethod
    def intersect(self, ray: Ray) -> Tuple[float, float]:
        pass

    @abstractmethod
    def normal(self, point: Point) -> Vector:
        pass
