from ..drawer import Color
from ..loader import FileLoadder


class Scene:
    def __init__(self, shapes=None):
        scene_new = FileLoadder.load_scene(self)
        self.shapes = shapes or []
        self.num_fig = int(scene_new[1])
        indexes = []
        for i in range(len(scene_new)):
            if scene_new[i] == '':
                indexes.append(i)
        else:
            indexes.append(len(scene_new))
        for i in range(self.num_fig):
            figure = scene_new[indexes[i] + 1: indexes[i + 1]]
            print(figure)
            self.form = figure[0].title()
            if figure[0] == "circle":
                self.x = int(figure[1])
                self.y = int(figure[2])
                self.radius = int(figure[3])
                self.color = Color(int(figure[4]), int(figure[5]), int(figure[6]))
            if figure[0] == "square":
                self.x = int(figure[1])
                self.y = int(figure[2])
                self.width = int(figure[3])
                self.height = int(figure[4])
                self.color = Color(int(figure[5]), int(figure[6]), int(figure[6]))
            if figure[0] == "line":
                self.x0 = int(figure[1])
                self.y0 = int(figure[2])
                self.x1 = int(figure[3])
                self.y1 = int(figure[4])
                self.color = Color(int(figure[5]), int(figure[6]), int(figure[7]))

    def add(self, new_shape):
        self.shapes.append(new_shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw()
