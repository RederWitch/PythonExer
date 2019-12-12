import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 3], [-1, 3]), [1, 3])
        self.assertEqual(add_frac([0, 3], [-3, 4]), [-3, 4])
        self.assertEqual(add_frac([-5, 4], [-2, 3]), [-23, 12])
        self.assertEqual(add_frac([6, 6], [2, 4]), [3, 2])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([2, 3], [-1, 3]), [1, 1])
        self.assertEqual(sub_frac([0, 3], [-3, 4]), [3, 4])
        self.assertEqual(sub_frac([-5, 4], [-2, 3]), [-7, 12])
        self.assertEqual(sub_frac([6, 6], [2, 4]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 3], [-1, 3]), [-2, 9])
        self.assertEqual(mul_frac([0, 3], [-3, 4]), self.zero)
        self.assertEqual(mul_frac([-5, 4], [-2, 3]), [5, 6])
        self.assertEqual(mul_frac([1, 2], [0, 3]), self.zero)
        self.assertEqual(mul_frac([6, 6], [2, 4]), [1, 2])


    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 3], [-1, 3]), [-2, 1])
        self.assertEqual(div_frac([2, 3], [1, -3]), [-2, 1])
        self.assertEqual(div_frac([0, 3], [-3, 4]), self.zero)
        self.assertEqual(div_frac([-5, 4], [-2, 3]), [15, 8])
        self.assertEqual(div_frac([1, 2], [0, 3]), None)
        self.assertEqual(div_frac([6, 6], [2, 4]), [2, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([-5, 1]), False)
        self.assertEqual(is_positive([0, 3]), False)
        self.assertEqual(is_positive([3, 4]), True)
        self.assertEqual(is_positive([7, 9]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([0, 7]), True)
        self.assertEqual(is_zero([-2, 4]), False)
        self.assertEqual(is_zero([5, 1]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([4, 5], [4, 5]), 0)
        self.assertEqual(cmp_frac([4, 3], [16, 12]), 0)
        self.assertEqual(cmp_frac([5, 8], [8, 10]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([5, 8]), float(5/8))
        self.assertEqual(frac2float([-1, 2]), float(-1/2))
        self.assertEqual(frac2float([2, 3]), float(2/3))
        self.assertEqual(frac2float([1, 10]), float(1/10))
        self.assertEqual(frac2float([0, 3]), float(0/3))
        self.assertEqual(frac2float([-21, 7]), float(-21/7))
        self.assertEqual(frac2float([8, 6]), float(8/6))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy