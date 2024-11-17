import math

from Figures.Point import Point


class Vector2D:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.pos = [(p2.x - p1.x), (p2.y - p1.y)]

    def get_length(self):
        return math.sqrt(self.pos[0] ** 2 +  self.pos[1] ** 2)

    def set_pos(self):
        self.pos = [(self.p2.x - self.p1.x), (self.p2.y - self.p1.y)]

    def move(self, vec):
        self.p1.x += vec.pos[0]
        self.p1.y += vec.pos[1]
        self.p2.x += vec.pos[0]
        self.p2.y += vec.pos[1]


    def rotate(self, p: Point, angle):
        x1_shifted = self.p1.x - p.x
        y1_shifted = self.p1.y - p.y
        x2_shifted = self.p2.x - p.x
        y2_shifted = self.p2.y - p.y

        new_x1 = x1_shifted * math.cos(angle) - y1_shifted * math.sin(angle)
        new_y1 = x1_shifted * math.sin(angle) + y1_shifted * math.cos(angle)

        new_x2 = x2_shifted * math.cos(angle) - y2_shifted * math.sin(angle)
        new_y2 = x2_shifted * math.sin(angle) + y2_shifted * math.cos(angle)

        self.p1 = Point(new_x1 + p.x, new_y1 + p.y)
        self.p2 = Point(new_x2 + p.x, new_y2 + p.y)
        self.set_pos()
