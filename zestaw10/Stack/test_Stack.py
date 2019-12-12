import unittest
from Stack import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.emptyS = Stack()
        self.stack = Stack()
        self.stack2 = Stack()
        self.stack2.push(1)
        self.stack2.push(2)
        self.stack2.push(333)

    def test_push_str(self):
        # empty stack []
        self.assertEqual(str(self.stack), "[]")
        # [1]
        self.stack.push(1)
        self.assertEqual(str(self.stack), "[1]")
        #[ 1, 2]
        self.stack.push(2)
        self.assertEqual(str(self.stack), "[1, 2]")
        #[ 1, 2, 333]
        self.stack.push(333)
        self.assertEqual(str(self.stack), "[1, 2, 333]")
        # [ 1, 2, 333]
        self.stack.push(333)
        self.assertEqual(str(self.stack), "[1, 2, 333, 333]")

    def test_is_empty(self):
        self.assertTrue(self.emptyS.is_empty())
        self.assertFalse(self.stack2.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.emptyS.is_full())

    def test_pop(self):
        self.assertRaises(ValueError, Stack().pop)
        self.assertRaises(ValueError, self.emptyS.pop)
        self.assertEqual(self.stack2.pop(), 333)
        self.assertEqual(self.stack2.pop(), 2)
        self.assertEqual(self.stack2.pop(), 1)


if __name__ == '__main__':
    unittest.main()
