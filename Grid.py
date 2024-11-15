from math import *

from My_Turtle import MyTurtle, MyScreen


def draw_grid(my_turtle: MyTurtle, my_screen: MyScreen):
    def draw_width(w, h):
        # drawing main line
        my_turtle.tur.teleport(-w / 2, 0)
        my_turtle.tur.setheading(0)
        my_turtle.tur.forward(w)

        # drawing
        my_turtle.tur.setheading(pi / 2)
        for i in range(0, w, 20):
            my_turtle.tur.teleport(-h / 2 + i, -5)
            my_turtle.tur.forward(10)


    def draw_height(h, w):
        my_turtle.tur.teleport(0, h / 2)
        my_turtle.tur.setheading(3 * pi / 2)
        my_turtle.tur.forward(h)

        my_turtle.tur.setheading(0)
        for i in range(0, w, 20):
            my_turtle.tur.teleport(-5, h / 2 - i)
            my_turtle.tur.forward(10)

    my_turtle.tur.color("red")
    width, height = my_screen.w, my_screen.h
    draw_width(width, height)
    draw_height(height, width)

    my_turtle.reset_turtle()



