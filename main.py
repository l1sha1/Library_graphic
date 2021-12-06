import random


from graphic.scene import Scene
from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Circle, Line, line
from graphic.shape.square import Square


def main():
    s = Scene()
    drawer = Drawer(256, 256)
    for i in range(s.num_fig):
        if s.figures[i][0] == "circle":
            s.add(Circle(s.figures[i][1], s.figures[i][2], s.figures[i][3], drawer, color=s.figures[i][4]))
        if s.figures[i][0] == "line":
            p_start = Point2D(s.figures[i][1], s.figures[i][2], drawer=drawer)
            p_end = Point2D(s.figures[i][3], s.figures[i][4], drawer=drawer)
            s.add(Line(p_start, p_end, drawer, color=s.figures[i][5]))
        if s.figures[i][0] == "square":
            s.add(Square(s.figures[i][1], s.figures[i][2], s.figures[i][3], s.figures[i][4], drawer, color=s.figures[i][5]))
        s.draw()
    drawer.save()


if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print("Координаты фигуры выходят за границы поля")
    except ValueError:
        print("Неверное значения цвета")
