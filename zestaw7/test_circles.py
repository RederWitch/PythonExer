from circles import Circle, pi
import unittest


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(0, 0, 4)
        self.c2 = Circle(0, 0, 2)
        self.c3 = Circle(2, 2, 2)
        self.c4 = Circle(3, 4, 2)

    def test_init(self):
        self.assertRaises(ValueError, Circle, 0, 0, -1)
        self.assertRaises(ValueError, Circle, 3, 3, -6)
        self.assertRaises(ValueError, Circle, 4, 6, -18)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(0, 0, 4)")
        self.assertEqual(repr(self.c2), "Circle(0, 0, 2)")
        self.assertEqual(repr(self.c3), "Circle(2, 2, 2)")

    def test_eq(self):
        self.assertTrue(self.c1 == Circle(0, 0, 4))
        self.assertTrue(self.c2 == Circle(0, 0, 2))
        self.assertTrue(self.c3 == Circle(2, 2, 2))
        self.assertFalse(self.c1 == Circle(4, 3, 2))

    def test_ne(self):
        self.assertTrue(self.c1 != Circle(0, 8, 2))
        self.assertTrue(self.c2 != Circle(3, 3, 3))
        self.assertTrue(self.c3 != Circle(12, 43, 123))
        self.assertFalse(self.c4 != Circle(3, 4, 2))

    def test_area(self):
        self.assertEqual(self.c1.area(), 16 * pi)
        self.assertEqual(self.c2.area(), 4 * pi)
        self.assertEqual(self.c3.area(), 4 * pi)

    def test_move(self):
        self.assertEqual(self.c1.move(2, 2), Circle(2, 2, 4))
        self.assertEqual(self.c2.move(1, 4), Circle(1, 4, 2))
        self.assertEqual(Circle(5, 5, 5).move(4, 5), Circle(9, 10, 5))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 4).cover(Circle(0, 0, 1)), Circle(0, 0, 4))
        self.assertEqual(Circle(0, 0, 5).cover(Circle(0, 4, 1)), Circle(0, 0, 5))
        self.assertEqual(Circle(0, 0, 2).cover(Circle(0, 3, 1)), Circle(0, 1, 3))
        self.assertEqual(Circle(0, 0, 1).cover(Circle(3, 4, 1)), Circle(1.5, 2, 3.5))
        self.assertEqual(Circle(1, 1, 2).cover(Circle(2, 1, 1)), Circle(1, 1, 2))



if __name__ == '__main__':
    unittest.main()

