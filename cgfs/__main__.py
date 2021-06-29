from cgfs.canvas import PillowCanvas
from cgfs.light.ambient_light import AmbientLight
from cgfs.light.directional_light import DirectionalLight
from cgfs.light.point_light import PointLight
from cgfs.raytracer import Raytracer
from cgfs.scene import Scene
from cgfs.scene_object.sphere import Sphere
from cgfs.viewport import Viewport

scene = Scene()

scene.add_object(Sphere((0, 0, 4), 1, (255, 0, 0), specular=20))
scene.add_object(Sphere((1, -1, 3), .5, (0, 255, 0), specular=200))
scene.add_object(Sphere((-.5, -.5, 3.5), .5, (0, 0, 255)))

scene.add_light(AmbientLight(.2))
scene.add_light(DirectionalLight((0, -5, 0), .3))
scene.add_light(PointLight((2, 10, -5), .8))

# book scene
# scene.add_light(AmbientLight(.2))
# scene.add_light(PointLight((2, 1, 0), .6))
# scene.add_light(DirectionalLight((1, 4, 4), .2))
#
# scene.add_object(Sphere((0, -1, 3), 1, (255, 0, 0), specular=500))
# scene.add_object(Sphere((2, 0, 4), 1, (0, 0, 255), specular=500))
# scene.add_object(Sphere((-2, 0, 4), 1, (0, 255, 0), specular=10))
# scene.add_object(Sphere((0, -5001, 0), 5000, (255, 255, 0), specular=100))

canvas = PillowCanvas(500, 500)
viewport = Viewport(1, 1, 1)

raytracer = Raytracer(scene, canvas, viewport)

raytracer.render()
canvas.show()
