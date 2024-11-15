from turtle import *

from Figures.Figure import Figure
from Geometry import *
from Math import *


class MyTurtle:
    def __init__(self):
        self.tur = Turtle()
        self.tur.radians()
        self.tur.speed(1)
        self.vertical_vector = Vector2D(Point(0, -1), Point(0, 1))
        self.horizontal_vector=  Vector2D(Point(-1, 0), Point(1, 0))

    def reset_turtle(self):
        self.tur.color("black")
        self.tur.teleport(0, 0)
        self.reset_rotation()

    def draw_vector(self, v: Vector2D):
        self.tur.teleport(v.p1.x, v.p1.y)
        self.rotate_turtle(v)
        self.tur.forward(v.get_length())
        self.reset_turtle()


    def draw_figure(self, fig: Figure):
        for v in fig.vectors:
            self.draw_vector(v)


    def reset_rotation(self):
        self.tur.setheading(0)


    def rotate_turtle(self, v: Vector2D):
        angle_to_rotate = angle_between(self.horizontal_vector, v)

        if v.pos[0] >= 0 and v.pos[1] >= 0:
            self.tur.left(angle_to_rotate)
        elif v.pos[0] < 0 <= v.pos[1]:
            self.tur.left(angle_to_rotate)
        elif v.pos[0] < 0 and v.pos[1] < 0:
            self.tur.left(2 * math.pi - angle_to_rotate)
        else:
            self.tur.left(2 * math.pi - angle_to_rotate)



    def show_turtle(self, show: bool, speed):
        if show:
            self.tur.showturtle()
            tracer(1)
        else:
            self.tur.hideturtle()
            tracer(0)
            self.tur.speed(speed)


class MyScreen:
    def __init__(self, w, h):
        self.w, self.h = w, h
        screen = Screen()
        screen.setup(width=w, height=h)

        root = screen._root
        root.resizable(False, False)

        update()
