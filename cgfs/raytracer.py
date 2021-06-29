from math import inf

from cgfs.canvas import Canvas
from cgfs.cgfs_types import Ray, Color
from cgfs.scene import Scene
from cgfs.viewport import Viewport


class Raytracer:
    BACKGROUND_COLOR: Color = (255, 255, 255)

    def __init__(self, scene: Scene, canvas: Canvas, viewport: Viewport):
        self._scene = scene
        self._canvas = canvas
        self._viewport = viewport
        self._camera_pos = (0, 0, 0)

    def render(self):
        for x, y, i in self._canvas.pixel_iterator():
            ray = self._ray(x, y)
            color = self._trace(ray, 1, inf)
            self._canvas.put_pixel(i, color)

    def _ray(self, x: int, y: int) -> Ray:
        return (self._camera_pos,
                (x * self._viewport.width / self._canvas.width,
                 y * self._viewport.height / self._canvas.height,
                 self._viewport.distance))

    def _trace(self, ray: Ray, t_min: float, t_max: float) -> Color:
        closest_t = inf
        closest_obj = None
        for obj in self._scene.scene_objects:
            for t in obj.intersect(ray):
                if t_min <= t <= t_max and t < closest_t:
                    closest_t = t
                    closest_obj = obj

        return closest_obj.color if closest_obj else self.BACKGROUND_COLOR
