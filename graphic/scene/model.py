from ..drawer import Color
from ..loader import FileLoadder


class Scene:
    def __init__(self, shapes=None):
        scene_new = FileLoadder.load_scene(self)
        self.shapes = shapes or []
        self.form = scene_new[2].title()
        self.num_fig = int(scene_new[1])
        if scene_new[2] == "circle":
            self.x = int(scene_new[3])
            self.y = int(scene_new[4])
            self.radius = int(scene_new[5])
            self.color = Color(int(scene_new[6]), int(scene_new[7]), int(scene_new[7]))

    def add(self, new_shape):
        self.shapes.append(new_shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw()
