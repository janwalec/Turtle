from Figures.Figure import Figure
from Geometry import Point, Vector2D


class Triangle(Figure):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
        self.vectors = [Vector2D(p1, p2), Vector2D(p2, p3), Vector2D(p3, p1)]
        self.middle_point = None
        self.set_middle_point()

    def set_middle_point(self):
        x, y = 0.0, 0.0
        for vector in self.vectors:
            x += vector.p1.x
            y += vector.p1.y

        self.middle_point = Point(x / 3, y / 3)

