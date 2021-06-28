from cgfs.scene import Scene
from cgfs.scene_object.sphere import Sphere

scene = Scene()
scene.add_object(Sphere((0, 0, 3), 1, (255, 0, 0)))
