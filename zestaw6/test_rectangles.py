import unittest
from rectangles import *


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec1 = Rectangle(2, 2, 6, 8)
        self.rec2 = Rectangle(-3, -6, 5, -2)
        self.rec3 = Rectangle(-4, 1, -1, 5)
        self.rec1Ko = Rectangle(2, 2, 6, 8)

    def test_print(self):
        self.assertEqual(str(self.rec1), "[(2, 2), (6, 8)]")
        self.assertEqual(str(self.rec2), "[(-3, -6), (5, -2)]")
        self.assertEqual(repr(self.rec1Ko), "Rectangle(2, 2), (6, 8)")
        self.assertEqual(repr(self.rec3), "Rectangle(-4, 1), (-1, 5)")

    def test_eq(self):
        self.assertTrue(self.rec1 == self.rec1Ko)
        self.assertFalse(self.rec1 == Rectangle(2, 2, 6, 17))
        self.assertFalse(self.rec1 == self.rec3)

    def test_ne(self):
        self.assertTrue(self.rec1 != self.rec3)
        self.assertTrue(self.rec3 != Rectangle(-4, 1, -1, 12))
        self.assertFalse(self.rec1 != self.rec1Ko)

    def test_center(self):
        self.assertEqual(self.rec1.center(), Point(4, 5))
        self.assertEqual(self.rec2.center(), Point(1, -4))
        self.assertEqual(self.rec3.center(), Point(-2.5, 3))

    def test_area(self):
        self.assertEqual(self.rec1.area(), 24)
        self.assertEqual(self.rec2.area(), 32)
        self.assertEqual(self.rec3.area(), 12)

    def test_move(self):
        self.assertEqual(self.rec1.move(2, 4), Rectangle(4, 6, 8, 12))
        self.assertEqual(self.rec2.move(-1, 2), Rectangle(-4, -4, 4, 0))
        self.assertEqual(self.rec3.move(-2, -3), Rectangle(-6, -2, -3, 2))
        self.assertEqual(self.rec1.move(4, -1), Rectangle(6, 1, 10, 7))


    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy