from cgfs.objects.scene_object import SceneObject


class Scene:
    def __init__(self):
        self._scene_objects = []

    def add_object(self, scene_object: SceneObject):
        self._scene_objects.append(scene_object)
