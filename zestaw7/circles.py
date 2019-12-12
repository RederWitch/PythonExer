from points import Point
from math import pi

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""
#center = Point(int x, int y)
#int radius

    def __init__(self, x, y, radius):
        if radius < 0:
            print("promień ujemny")
            raise ValueError
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        return pi*self.radius*self.radius

    def move(self, x, y):    # przesuniecie o (x, y)
        a = self.pt.x + x
        b = self.pt.y + y
        return Circle(a, b, self.radius)

    def cover(self, other):    # okrąg pokrywający oba
        if self.pt.distance(other.pt) <= (max(self.radius, other.radius) - min(self.radius, other.radius)):
            if other.radius >= self.radius:
                return other
            else:
                return self

        x = (self.pt.x + other.pt.x) / 2
        y = (self.pt.y + other.pt.y) / 2
        vector = Point(x / Point(x, y).length(), y / Point(x, y).length())
        center = Point()
        center.x = vector.x * (self.radius + other.radius + \
                               Point(self.pt.x, self.pt.y).distance(
                                   Point(other.pt.x, other.pt.y))) / 2 - self.radius * vector.x
        center.y = vector.y * (self.radius + other.radius + \
                               Point(self.pt.x, self.pt.y).distance(
                                   Point(other.pt.x, other.pt.y))) / 2 - self.radius * vector.y
        rad = center.distance(self.pt) + self.radius
        return Circle(center.x, center.y, rad)

#distance to funkcja licząca odległość między dwoma punktami,"
#znajduje się w clasie Point"
#    def distance(self, other):
#       return sqrt((self.x-other.x)**2+(self.y-other.y)**2)"