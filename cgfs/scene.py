from typing import List

from cgfs.light import Light
from cgfs.scene_object import SceneObject


class Scene:
    def __init__(self):
        self.scene_objects: List[SceneObject] = []
        self.lights: List[Light] = []

    def add_object(self, scene_object: SceneObject):
        self.scene_objects.append(scene_object)

    def add_light(self, light: Light):
        self.lights.append(light)
