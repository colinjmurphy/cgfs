from abc import ABC, abstractmethod

from cgfs.types import Color, Ray


class SceneObject(ABC):
    @abstractmethod
    @property
    def color(self) -> Color:
        pass

    @abstractmethod
    def intersect(self, ray: Ray):
        pass