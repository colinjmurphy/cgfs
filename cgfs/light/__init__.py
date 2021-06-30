from abc import abstractmethod
from typing import List

from cgfs.cgfs_types import Point, Vector
from cgfs.scene_object import SceneObject
from cgfs.utils import sub, scale, dot, length


class Light:
    def __init__(self, intensity: float):
        self._intensity = intensity

    @abstractmethod
    def illuminate(self, point: Point, camera_direction: Vector, scene_object: SceneObject,
                   scene_objects: List[SceneObject]) -> float:
        pass

    def _specular(self, object_normal: Vector, light_direction: Vector, camera_direction: Vector,
                  specular: float, n_dot_l: float):
        r = sub(scale(object_normal, 2 * n_dot_l), light_direction)
        r_dot_v = dot(r, camera_direction)
        if r_dot_v > 0:
            return self._intensity * pow(r_dot_v / (length(r) * length(camera_direction)), specular)
        else:
            return 0
