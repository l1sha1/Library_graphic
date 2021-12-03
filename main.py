import random


from graphic.scene import Scene
from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Circle, Line, line
from graphic.shape.square import Square


def main():
    s = Scene()

    drawer = Drawer(256, 256)
    for i in range(s.num_fig):
        if s.figure_i[0] == "circle":
            s.add(Circle(s.x, s.y, s.radius, drawer, color=s.color))
        if s.figure_i[0] == "line":
            p_start = Point2D(s.x0, s.y0, drawer=drawer)
            print(s.x0)
            p_end = Point2D(s.x1, s.y1, drawer=drawer)
            s.add(Line(p_start, p_end, drawer, color=s.color))
        if s.figure_i[0] == "square":
            print(s.height)
            s.add(Square(s.x, s.y, s.width, s.height, drawer, color=s.color))
        s.draw()

    drawer.save()


if __name__ == '__main__':
    main()
