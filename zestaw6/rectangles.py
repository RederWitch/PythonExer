#Zestaw 6 zad 3
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}), ({}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        point = Point()
        point.x = (self.pt1.x + self.pt2.x)/2.0
        point.y = (self.pt1.y + self.pt2.y)/2.0
        return point

    def area(self):            # pole powierzchni
        return (self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        rectangle = Rectangle()
        rectangle.pt1.x = self.pt1.x + x
        rectangle.pt1.y = self.pt1.y + y
        rectangle.pt2.x = self.pt2.x + x
        rectangle.pt2.y = self.pt2.y + y
        return rectangle
