import unittest
from points import *
from math import sqrt

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, -2)), "(1, -2)")
        self.assertEqual(str(Point(18, 0)), "(18, 0)")
        self.assertEqual(repr(Point(5, 7)), "Point(5, 7)")
        self.assertEqual(repr(Point(-3, 3)), "Point(-3, 3)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(30, 5) == Point(30, 50))
        self.assertFalse(Point(6, 4) == Point(5, 8))

    def test_ne(self):
        self.assertFalse(Point(3, 5) != Point(3, 5))
        self.assertTrue(Point(30, 3) != Point(30, 20))
        self.assertTrue(Point(-12, 4) != Point(-3, 1))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(2, 5), Point(3, 7))
        self.assertEqual(Point(10, 12) + Point(-2, 5), Point(8, 17))
        self.assertEqual(Point(-6, 4) + Point(6, 9), Point(0, 13))
        self.assertEqual(Point(-5, 8) + Point(-3, 0), Point(-8, 8))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(2, 5), Point(-1, -3))
        self.assertEqual(Point(10, 12) - Point(-2, 5), Point(12, 7))
        self.assertEqual(Point(-6, 4) - Point(6, 9), Point(-12, -5))
        self.assertEqual(Point(-5, 8) - Point(-3, 0), Point(-2, 8))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(2, 5), 12)
        self.assertEqual(Point(10, 12) * Point(-2, 5), 40)
        self.assertEqual(Point(-6, 4) * Point(6, 9), 0)
        self.assertEqual(Point(-5, 8) * Point(-3, 0), 15)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(2, 5)), 1)
        self.assertEqual(Point(10, 12).cross(Point(-2, 5)), 74)
        self.assertEqual(Point(-6, 4).cross(Point(6, 9)), -78)
        self.assertEqual(Point(-5, 8).cross(Point(-3, 0)), 24)
        self.assertEqual(Point(-3, -4).cross(Point(-6, -7)), -3)

    def test_length(self):
        self.assertEqual(Point(8, 6).length(), 10)
        self.assertEqual(Point(-1, 0).length(), 1)
        self.assertEqual(Point(3, -4).length(), 5)
        self.assertEqual(Point(-3, 7).length(), sqrt(58))


    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy