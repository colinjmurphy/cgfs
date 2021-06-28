from cgfs.objects.scene_object import SceneObject
from cgfs.types import Ray, Color


class Sphere(SceneObject):
    def __init__(self, color: Color):
        self._color = color

    @property
    def color(self) -> Color:
        return self._color

    def intersect(self, ray: Ray):
        pass
