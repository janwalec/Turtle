from Geometry import *


class Figure:
    def __init__(self):
        self.vectors = None
        self.vectors = []


    def set_middle_point(self):
        raise Exception("not implemented")

    def move(self, v: Vector2D):
        for vector in self.vectors:
            vector.move(v)
        self.set_middle_point()

    def rotate_by_point_and_angle(self, p: Point, angle):
        for v in self.vectors:
            v.rotate(p, angle)
        self.set_middle_point()