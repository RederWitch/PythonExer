import unittest
from queue import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(2)
        self.queue.put(1)
        self.queue.put(999)
        self.queue2 = Queue(3)
        self.queue2.put(222)

    def test_init(self):
        self.assertRaises(ValueError, Queue, 0)
        self.assertRaises(ValueError, Queue, -6)

    def test_is_empty(self):
        self.assertTrue(Queue().is_empty())
        self.assertTrue(Queue(9).is_empty())
        self.assertFalse(self.queue.is_empty())
        self.assertFalse(self.queue2.is_empty())

    def test_is_full(self):
        self.assertFalse(Queue().is_full())
        self.assertFalse(Queue(2).is_full())
        self.assertFalse(self.queue2.is_full())
        self.assertTrue(self.queue.is_full())

    def test_put(self):
        self.assertRaises(ValueError, self.queue.put, 12)

    def test_get(self):
        self.assertRaises(ValueError, Queue().get)
        self.assertRaises(ValueError, Queue(3).get)
        self.assertEqual(self.queue.get(), 1)

if __name__ == '__main__':
    unittest.main()
