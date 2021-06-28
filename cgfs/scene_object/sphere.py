from cgfs.scene_object import SceneObject
from cgfs.types import Ray, Color, Point


class Sphere(SceneObject):
    def __init__(self, center: Point, radius: float, color: Color):
        self._center = center
        self._radius = radius
        self._color = color

    @property
    def color(self) -> Color:
        return self._color

    def intersect(self, ray: Ray):
        pass
