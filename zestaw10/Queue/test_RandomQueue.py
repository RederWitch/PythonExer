import unittest
from RandomQueue import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue(5)
        self.queue.insert(1)
        self.queue.insert(22)
        self.queue.insert(333)
        self.queue.insert(4444)
        self.queue.insert(55555)
        self.queue2 = RandomQueue()
        self.queue2.insert(8)
        self.emptyq = RandomQueue()

    def test_init(self):
        self.assertRaises(ValueError, RandomQueue, 0)
        self.assertRaises(ValueError, RandomQueue, -4)

    def test_is_empty(self):
        self.assertTrue(RandomQueue().is_empty())
        self.assertTrue(RandomQueue(5).is_empty())
        self.assertTrue(self.emptyq.is_empty())
        self.assertFalse(self.queue.is_empty())
        self.assertFalse(self.queue2.is_empty())
        self.queue2.remove()
        self.assertTrue(self.queue2.is_empty())

    def test_is_full(self):
        self.assertTrue(self.queue.is_full())
        self.assertFalse(self.queue2.is_full())
        self.assertFalse(self.emptyq.is_full())

    def test_insert(self):
        self.assertRaises(IndexError, self.queue.insert, 9)

    def test_remove(self):
        self.assertRaises(IndexError, self.emptyq.remove)
        for item in range(5):
            self.assertNotEqual(None, self.queue.remove())


    def test_clear(self): pass


if __name__ == '__main__':
    unittest.main()
