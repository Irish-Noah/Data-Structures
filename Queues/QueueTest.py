from Queue import Queue
import unittest

class QueueTest(unittest.TestCase):

    def test_empty(self):
        queue = Queue()
        self.assertTrue(queue.empty())

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size, 0)
        queue.push(1)
        self.assertEqual(queue.size, 1)
        queue.pop()
        self.assertEqual(queue.size, 0)

    def test_push_pop(self):
        queue = Queue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)

        # check top most elem
        self.assertEqual(queue.top(), 1)

        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 4)

        # should be none when empty
        self.assertIsNone(queue.pop())
