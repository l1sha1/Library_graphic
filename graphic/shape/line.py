from . import Point2D
from .shape import Shape
from ..drawer import Color


class Line(Shape):
    line_counter = 0

    def __init__(self, start, end, drawer, color=None):
        Shape.__init__(self, drawer)
        self.start = start
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
        xi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        if dx < 0:
            xi = -1
            dx = -dx
        d = 2 * dy - dx
        if dx != 0 and dy != 0:
            y = self.start.y
            for x in range(self.start.x, self.end.x + 1):
                self.drawer.put_pixel(x, y, self.color)
                if d > 0:
                    y = y + yi
                    d = d + (2 * (dy - dx))
                else:
                    d = d + 2 * dy
        elif dx == 0:
            x = self.start.x - 1
            for y in range(self.start.y + 1, self.end.y + 1):
                self.drawer.put_pixel(x, y, self.color)
                if d > 0:
                    x = x + xi
                    d = d + (2 * (dx - dy))
                else:
                    d = d + 2 * dx
        elif dy == 0:
            y = self.start.y + 1
            for x in range(self.start.x, self.end.x + 1):
                self.drawer.put_pixel(x, y, self.color)
                if d > 0:
                    y = y + yi
                    d = d + (2 * (dy - dx))
                else:
                    d = d + 2 * dy

