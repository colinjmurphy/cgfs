from typing import List

from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light
from cgfs.scene_object import SceneObject


class AmbientLight(Light):
    def illuminate(self, point: Point, camera_direction: Vector, scene_object: SceneObject,
                   scene_objects: List[SceneObject]) -> float:
        return self._intensity
