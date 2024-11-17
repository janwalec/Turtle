from Figures.Triangle import Triangle
from Grid import draw_grid
from My_Turtle import *


class SceneController:
    def __init__(self):
        self.my_screen = MyScreen(800, 800)
        self.my_turtle = MyTurtle()
        self.my_turtle.show_turtle(False, spd=1)

    def move_forward(self):
        self.my_turtle.absolute_position.x += 1
        print(self.my_turtle.absolute_position.x)


    def main_loop(self):

        while(True):
            self.my_turtle.tur.clear()

            self.what_to_draw()
            self.my_screen.screen.listen()
            self.my_screen.screen.onkey(self.move_forward, "w")


            update()



    def what_to_draw(self):
        draw_grid(self.my_turtle, self.my_screen)

        A = Point(30, 50)
        B = Point(80, 60)
        C = Point(100, 20)
        D = Point(30, -50)
        t1 = Triangle(A, B, C)
        t2 = Triangle(C, D, A)
        self.my_turtle.draw_figure(t1)
        self.my_turtle.draw_figure(t2)

        t1.rotate_by_point_and_angle(Point(0, 0), math.pi / 2)
        t2.rotate_by_point_and_angle(Point(0, 0), math.pi / 2)
        self.my_turtle.draw_figure(t1)
        self.my_turtle.draw_figure(t2)


    @staticmethod
    def end():
        update()
        done()
        bye()
        print("bye")
