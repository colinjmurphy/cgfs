from cgfs.canvas import PillowCanvas
from cgfs.raytracer import Raytracer
from cgfs.scene import Scene
from cgfs.scene_object.sphere import Sphere
from cgfs.viewport import Viewport

scene = Scene()
scene.add_object(Sphere((0, 0, 4), 1, (255, 0, 0)))
scene.add_object(Sphere((1, -1, 3), .5, (0, 255, 0)))
scene.add_object(Sphere((-.5, -.5, 3.5), .5, (0, 0, 255)))

canvas = PillowCanvas(500, 500)
viewport = Viewport(1, 1, 1)

raytracer = Raytracer(scene, canvas, viewport)

raytracer.render()
canvas.show()
