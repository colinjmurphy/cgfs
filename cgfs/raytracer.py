from cgfs.canvas import Canvas
from cgfs.scene import Scene
from cgfs.types import Ray
from cgfs.viewport import Viewport


class Raytracer:
    def __init__(self, scene: Scene, canvas: Canvas, viewport: Viewport):
        self._scene = scene
        self._canvas = canvas
        self._viewport = viewport
        self._camera_pos = (0, 0, 0)

    def render(self):
        for y in range(-self._canvas.half_height, self._canvas.half_height):
            for x in range(-self._canvas.half_width, self._canvas.half_width):
                ray = self._ray(x, y)
                color = self._trace(ray, 1, 100000)

    def _ray(self, x: int, y: int) -> Ray:
        return (self._camera_pos,
                (x * self._viewport.width / self._canvas.width,
                 y * self._viewport.height / self._canvas.height,
                 self._viewport.distance))

    def _trace(self, ray: Ray, t_min: int, t_max: int):
        for obj in self._scene.scene_objects:
            pass
