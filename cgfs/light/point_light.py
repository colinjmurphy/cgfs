from typing import List

from cgfs.cgfs_types import Point, Vector
from cgfs.light import Light
from cgfs.scene_object import SceneObject
from cgfs.utils import dot, sub, length, EPSILON


class PointLight(Light):
    def __init__(self, location: Point, intensity: float):
        super().__init__(intensity)
        self._location = location

    def illuminate(self, point: Point, camera_direction: Vector, scene_object: SceneObject,
                   scene_objects: List[SceneObject]) -> float:
        light_direction = sub(self._location, point)
        ray = (point, light_direction)
        for obj in scene_objects:
            for _ in obj.intersect(ray, EPSILON, 1):
                # shadowed
                return 0

        object_normal = scene_object.normal(point)
        n_dot_l = dot(object_normal, light_direction)

        illumination = self._intensity * n_dot_l / length(light_direction)

        if scene_object.specular is not None:
            illumination += max(
                self._specular(object_normal, light_direction, camera_direction, scene_object.specular), 0
            )

        return illumination
