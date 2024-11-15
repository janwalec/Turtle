
from Figures.Triangle import Triangle
from Math import *
from Geometry import *
from My_Turtle import *
from Grid import *






my_screen = MyScreen(800, 800)
my_turtle = MyTurtle()

my_turtle.show_turtle(False, speed=1)
draw_grid(my_turtle, my_screen)



B = Point(100, 80)
A = Point(80, 80)
C = Point(100, 60)

t = Triangle(A, B, C)





#t.rotate_by_point_and_angle(to_radians(60), t.middle_point)

#my_turtle.draw_figure(t)


j = 20

while j >= -15:
    j -= 5
    t.move(Vector2D(Point(0, 0), Point(j * math.pi, j * math.pi)))
    for i in range(0, 360, 30):
        t.rotate_by_point_and_angle(Point(0,0), to_radians(i))
        my_turtle.draw_figure(t)
        t.rotate_by_point_and_angle(Point(0,0), to_radians(-i))



update()
done()

