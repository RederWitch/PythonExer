
#Zestaw 6 zad 2
from math import sqrt


class Point:
    # Klasa reprezentująca punkty na płaszczyźnie.

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.

    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):         # długość wektora
        return sqrt(self.x*self.x + self.y*self.y)

    def distance(self, other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
