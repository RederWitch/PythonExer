from zad4 import heron, sqrt
import unittest


class TestCircle(unittest.TestCase):

    def setUp(self): pass

    def test_heron(self):
        self.assertRaises(ValueError, heron, 2, 3, 7)
        self.assertRaises(ValueError, heron, 1, 5, 4)
        self.assertRaises(ValueError, heron, 15, 3, 7)
        self.assertEqual(heron(4, 3, 5), 6)
        self.assertEqual(heron(5, 5, 6), 12)
        self.assertEqual(heron(3, 7, 6), 4*sqrt(5))

if __name__ == '__main__':
    unittest.main()
