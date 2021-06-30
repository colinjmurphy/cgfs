from math import sqrt

from cgfs.cgfs_types import Point, Vector, Color

EPSILON = 0.001


def normalize(vector: Vector) -> Vector:
    magnitude = length(vector)
    return vector[0] / magnitude, vector[1] / magnitude, vector[2] / magnitude


def length(vector: Vector) -> float:
    return sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])


def scale(a: Vector, scalar: float):
    return a[0] * scalar, a[1] * scalar, a[2] * scalar


def scale_color(a: Color, scalar: float):
    return tuple(max(min(int(i * scalar), 255), 0) for i in a)


def add(a: Point, b: Point) -> Point:
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def sub(a: Point, b: Point) -> Point:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def dot(a: Point, b: Point) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
