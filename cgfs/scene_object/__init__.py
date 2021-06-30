from abc import ABC, abstractmethod
from math import inf
from typing import Iterable

from cgfs.cgfs_types import Color, Ray, Point, Vector


class SceneObject(ABC):
    def __init__(self, color: Color, specular: float):
        self._color = color
        self._specular = specular

    @property
    def color(self) -> Color:
        return self._color

    @property
    def specular(self) -> float:
        return self._specular

    @abstractmethod
    def intersect(self, ray: Ray, t_min: float = -inf, t_max: float = inf) -> Iterable[float]:
        pass

    @abstractmethod
    def normal(self, point: Point) -> Vector:
        pass
