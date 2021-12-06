from .shape import Shape
from ..drawer import Color
from ..scene import Scene


class Circle(Shape, Scene):
    line_counter = 0

    def __init__(self, x, y, radius, drawer, color=None):
        Shape.__init__(self, drawer)
        self.x = x
        self.y = y + radius
        self.radius = radius
        self.color = color or Color(255, 255, 255)

    # @staticmethod
    # def stat():
    #   print(f"{Line.line_counter} was created")

    def draw(self):
        disp_x = self.x
        disp_y = self.y - self.radius
        x = 0
        y = self.radius
        delta = (1 - 2 * self.radius)
        error = 0
        while y >= 0:
            self.drawer.put_pixel(disp_x + x, disp_y + y, self.color)
            self.drawer.put_pixel(disp_x + x, disp_y - y, self.color)
            self.drawer.put_pixel(disp_x - x, disp_y + y, self.color)
            self.drawer.put_pixel(disp_x - x, disp_y - y, self.color)
            error = 2 * (delta + y) - 1
            if (delta < 0) and (error <= 0):
                x += 1
                delta = delta + (2 * x + 1)
                continue
            error = 2 * (delta - x) - 1
            if (delta > 0) and (error > 0):
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1
