from typing import List

from cgfs.scene_object import SceneObject


class Scene:
    def __init__(self):
        self.scene_objects: List[SceneObject] = []

    def add_object(self, scene_object: SceneObject):
        self.scene_objects.append(scene_object)
