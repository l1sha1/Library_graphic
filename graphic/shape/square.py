from graphic.drawer import Color
from graphic.shape import Shape, Point2D, Line


class Square(Shape):
    def __init__(self, x, y, w, h, drawer, color=None):
        Shape.__init__(self, drawer)
        self.start = None
        self.end = None
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color or Color(255, 255, 255)

    def draw(self):
        from graphic import drawer
        self.start = Point2D(self.x, self.y, drawer)
        self.end = Point2D(self.x, self.y + self.width, drawer)
        point_3 = Point2D(self.x + self.height, self.y + self.width, drawer)
        point_4 = Point2D(self.x + self.height, self.y, drawer)
        print(f'self.height in SQUARE = {self.height}')
        print(type(self.start.x))
        Line(self.start, self.end, drawer, color=self.color)
