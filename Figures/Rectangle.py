from Figures.Figure import Figure
from Figures.Point import Point
from Figures.Vector2D import Vector2D


class Rectangle(Figure):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        super().__init__()
        self.vectors = [Vector2D(p1, p2), Vector2D(p2, p3), Vector2D(p3, p4), Vector2D(p4, p1)]
        self.set_middle_point()

    def set_middle_point(self):
        x, y = 0.0, 0.0
        for vector in self.vectors:
            x += vector.p1.x
            y += vector.p1.y

        self.middle_point = Point(x / 3, y / 3)

