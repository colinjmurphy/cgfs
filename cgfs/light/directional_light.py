from math import inf
from typing import List

from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light
from cgfs.scene_object import SceneObject
from cgfs.utils import dot, normalize, EPSILON


class DirectionalLight(Light):
    def __init__(self, direction: Vector, intensity: float):
        super().__init__(intensity)
        self._light_direction = normalize(direction)

    def illuminate(self, point: Point, camera_direction: Vector, scene_object: SceneObject,
                   scene_objects: List[SceneObject]) -> float:
        ray = (point, self._light_direction)
        for obj in scene_objects:
            for _ in obj.intersect(ray, EPSILON, inf):
                # shadowed
                return 0

        object_normal = scene_object.normal(point)
        n_dot_l = dot(object_normal, self._light_direction)

        illumination = max(self._intensity * n_dot_l, 0)
        if scene_object.specular is not None:
            illumination += max(
                self._specular(object_normal, self._light_direction, camera_direction, scene_object.specular, n_dot_l), 0
            )

        return illumination
