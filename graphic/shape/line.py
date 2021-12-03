from . import Point2D
from .shape import Shape
from ..drawer import Color


class Line(Shape):
    line_counter = 0

    def __init__(self, start, end, drawer, color=None):
        Shape.__init__(self, drawer)
        self.start = start
        print(f'self.start={self.start}')
        self.end = end
        self.line_counter += 1
        self.color = color or Color(255, 255, 255)

    @staticmethod
    def stat():
        print(f"{Line.line_counter} was created")

    def draw(self):
        """ Realization of Bresenham's algorithm for drawing lines
        """
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2 * dy - dx
        y = self.start.y
        for x in range(self.start.x, self.end.x + 1):
            self.drawer.put_pixel(x, y, self.color)
            if D > 0:
                y = y + yi
                D = D + (2 * (dy - dx))
            else:
                D = D + 2 * dy
