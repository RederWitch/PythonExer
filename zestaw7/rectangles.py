from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if not (x1 < x2):
            print("Bledny X2")
            raise ValueError
        if not (y1 < y2):
            print("Bledny Y2")
            raise ValueError
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}), ({}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):         # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):                # zwraca środek prostokąta
        point = Point()
        point.x = (self.pt1.x + self.pt2.x) / 2.0
        point.y = (self.pt1.y + self.pt2.y) / 2.0
        return point

    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        x1 = self.pt1.x + x
        y1 = self.pt1.y + y
        x2 = self.pt2.x + x
        y2 = self.pt2.y + y
        rectangle = Rectangle(x1, y1, x2, y2)
        return rectangle

    def intersection(self, other): # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        try:
            rect = Rectangle(x1, y1, x2, y2)
        except ValueError:
            print("Brak części wspólnej")
            return None
        else:
            return rect

    def cover(self, other):         # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        bigger = Rectangle(x1, y1, x2, y2)
        return bigger

    def make4(self):                   # zwraca listę czterech mniejszych
        rectList =list()
        center = self.center()
        a = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        rectList.append(a)
        b = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        rectList.append(b)
        c = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        rectList.append(c)
        d = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        rectList.append(d)
        return rectList
