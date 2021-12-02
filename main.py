import random


from graphic.scene import Scene
from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Circle


def main():
    s = Scene()
    drawer = Drawer(256, 256)
    print(s.num_fig)
    print(s.shapes)
    for i in range(s.num_fig):
        fun = eval(s.form)
        s.add(fun(s.x, s.y, s.radius, drawer, color=s.color))
    s.draw()

    drawer.save()


if __name__ == '__main__':
    main()
