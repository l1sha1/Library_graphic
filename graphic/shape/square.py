from graphic.drawer import Color
from graphic.shape import Shape, Point2D, Line


class Square(Line):
    def __init__(self, x, y, w, h, drawer, color=None):
        Shape.__init__(self, drawer)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color or Color(255, 255, 255)
        self.point_1 = Point2D(self.x, self.y, drawer)
        self.point_2 = Point2D(self.x, self.y + self.width, drawer)
        self.point_3 = Point2D(self.x + self.height, self.y + self.width, drawer)
        self.point_4 = Point2D(self.x + self.height, self.y, drawer)
        self.l_1 = Line(self.point_1, self.point_2, drawer, color=self.color)
        self.l_2 = Line(self.point_2, self.point_3, drawer, color=self.color)
        self.l_3 = Line(self.point_4, self.point_3, drawer, color=self.color)
        self.l_4 = Line(self.point_1, self.point_4, drawer, color=self.color)

    def draw(self):
        self.l_1.draw()
        self.l_2.draw()
        self.l_3.draw()
        self.l_4.draw()



