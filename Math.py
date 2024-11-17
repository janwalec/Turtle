from Figures.Vector2D import Vector2D
import math

def dot_product(v1: Vector2D, v2: Vector2D):
    return v1.pos[0] * v2.pos[0] + v1.pos[1] * v2.pos[1]

def angle_between(v1: Vector2D, v2: Vector2D):
        c = dot_product(v1, v2) / (v1.get_length() * v2.get_length())
        return math.acos(c)

def to_degrees(rad):
    return rad * 180.0 / math.pi

def to_radians(deg):
    return deg * math.pi / 180.0