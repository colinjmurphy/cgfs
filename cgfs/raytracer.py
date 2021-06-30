from math import inf

from cgfs.canvas import Canvas
from cgfs.cgfs_types import Ray, Color
from cgfs.scene import Scene
from cgfs.utils import scale, scale_color, sub, reflect, EPSILON, add_color, negate, add
from cgfs.viewport import Viewport


class Raytracer:
    # BACKGROUND_COLOR: Color = (255, 255, 255)
    BACKGROUND_COLOR: Color = (0, 0, 0)

    def __init__(self, scene: Scene, canvas: Canvas, viewport: Viewport):
        self._scene = scene
        self._canvas = canvas
        self._viewport = viewport
        self._camera_pos = (0, 0, 0)

    def render(self):
        for x, y, i in self._canvas.pixel_iterator():
            ray = self._ray(x, y)
            color = self._trace(ray, 1, inf, 3)
            self._canvas.put_pixel(i, color)

    def _ray(self, x: int, y: int) -> Ray:
        return (self._camera_pos,
                (x * self._viewport.width / self._canvas.width,
                 y * self._viewport.height / self._canvas.height,
                 self._viewport.distance))

    def _trace(self, ray: Ray, t_min: float, t_max: float, recursion_depth: int) -> Color:
        closest_t = inf
        closest_obj = None
        for obj in self._scene.scene_objects:
            for t in obj.intersect(ray, t_min, t_max):
                if t < closest_t:
                    closest_t = t
                    closest_obj = obj

        if closest_obj:
            point = add(ray[0], scale(ray[1], closest_t))
            camera_direction = sub(ray[0], ray[1])

            intensity = 0.0
            for light in self._scene.lights:
                intensity += light.illuminate(point, camera_direction, closest_obj, self._scene.scene_objects)

            local_color = scale_color(closest_obj.color, intensity)
            if closest_obj.reflective > 0 and recursion_depth > 0:
                r = reflect(negate(ray[1]), closest_obj.normal(point))
                reflected_color = self._trace((point, r),
                                              EPSILON, inf, recursion_depth - 1)

                return add_color(
                    scale_color(reflected_color, closest_obj.reflective),
                    scale_color(local_color, 1 - closest_obj.reflective)
                )
            else:
                return local_color

        else:
            return self.BACKGROUND_COLOR
