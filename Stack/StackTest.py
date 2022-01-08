from Stack import Stack
import unittest

class StackTest(unittest.TestCase):

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size, 0)
        stack.push(1)
        self.assertEqual(stack.size, 1)
        stack.pop()
        self.assertEqual(stack.size,0)

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        # check top most elem
        self.assertEqual(stack.top(), 4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

        # should be none when empty 
        self.assertIsNone(stack.pop())
