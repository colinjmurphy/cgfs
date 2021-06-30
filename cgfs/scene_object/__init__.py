from abc import ABC, abstractmethod
from math import inf
from typing import Iterable

from cgfs.cgfs_types import Color, Ray, Point, Vector


class SceneObject(ABC):
    def __init__(self, color: Color, specular: float, reflective: float):
        self._color = color
        self._specular = specular
        self._reflective = reflective

    @property
    def color(self) -> Color:
        return self._color

    @property
    def specular(self) -> float:
        return self._specular

    @property
    def reflective(self) -> float:
        return self._reflective

    @abstractmethod
    def intersect(self, ray: Ray, t_min: float = -inf, t_max: float = inf) -> Iterable[float]:
        pass

    @abstractmethod
    def normal(self, point: Point) -> Vector:
        pass
