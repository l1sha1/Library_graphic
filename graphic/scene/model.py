from ..drawer import Color
from ..loader import FileLoadder


class Scene(FileLoadder):

    def __init__(self, shapes=None):
        self.form = None
        self.scene_new = FileLoadder.load_scene(self)
        self.shapes = shapes or []
        self.num_fig = int(self.scene_new[1])
        self.indexes = []
        for i in range(len(self.scene_new)):
            if self.scene_new[i] == '':
                self.indexes.append(i)
        else:
            self.indexes.append(len(self.scene_new))
        self.figures = []
        for i in range(self.num_fig):
            print(i)
            self.figure_i = self.scene_new[self.indexes[i] + 1: self.indexes[i + 1]]
            self.form = self.scene_new[self.indexes[i] + 1]
            if self.figure_i[0] == "circle":
                self.x = int(self.figure_i[1])
                self.y = int(self.figure_i[2])
                self.radius = int(self.figure_i[3])
                self.color = Color(int(self.figure_i[4]), int(self.figure_i[5]), int(self.figure_i[6]))
                circle_new = [self.figure_i[0], self.x, self.y, self.radius, self.color]
                self.figures.append(circle_new)
            if self.figure_i[0] == "square":
                self.x = int(self.figure_i[1])
                self.y = int(self.figure_i[2])
                self.width = int(self.figure_i[3])
                self.height = int(self.figure_i[4])
                self.color = Color(int(self.figure_i[5]), int(self.figure_i[6]), int(self.figure_i[6]))
                square_new = [self.figure_i[0], self.x, self.y, self.width, self.height, self.color]
                self.figures.append(square_new)
            if self.figure_i[0] == "line":
                self.x0 = int(self.figure_i[1])
                self.y0 = int(self.figure_i[2])
                self.x1 = int(self.figure_i[3])
                self.y1 = int(self.figure_i[4])
                self.color = Color(int(self.figure_i[5]), int(self.figure_i[6]), int(self.figure_i[7]))
                line_new = [self.figure_i[0], self.x0, self.y0, self.x1, self.y1, self.color]
                self.figures.append(line_new)

    def add(self, new_shape):
        self.shapes.append(new_shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw()
