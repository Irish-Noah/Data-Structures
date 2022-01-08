from SinglyLinkedList import SLL, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_node(self):
        node = Node()
        self.assertIsNone(node.next)
        self.assertIsNone(node.val)

        node = Node(50)
        self.assertIsNone(node.next)
        self.assertEqual(node.val, 50)


class SLLTest(unittest.TestCase):

    def test_empty(self):
        sll = SLL()
        self.assertEqual(True, sll.empty())

    def test_add(self):
        sll = SLL()
        sll.add_node(1)

        self.assertEqual(1, sll.head.val)
        self.assertEqual(1, sll.tail.val)

        sll.add_node(2)

        self.assertEqual(1, sll.head.val)
        self.assertEqual(2, sll.tail.val)

        sll.add_node(3)

        self.assertEqual(1, sll.head.val)
        self.assertEqual(3, sll.tail.val)

