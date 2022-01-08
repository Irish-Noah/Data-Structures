from DoublyLinkedList import DLL, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_node(self):
        node = Node(50)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        self.assertEqual(node.value, 50)

"""
    !!! I did not write these test cases. They were written by my professor for testing
    a doubly linked list !!!
    
    I used this code to prove that the DLL I wrote does, in fact, work at the level that 
    my professor would have wanted it to.
"""

class DLLTest(unittest.TestCase):

    def test_empty(self):
        # (1) empty DLL
        dll = DLL()
        self.assertTrue(dll.empty())

        # (2) DLL with one node
        dll.head = dll.tail = Node(1)
        dll.size += 1
        self.assertFalse(dll.empty())

        # (3) DLL with multiple nodes
        for i in range(0, 50):
            dll.tail.next = Node(i, None, dll.tail)
            dll.tail = dll.tail.next
            dll.size += 1
            self.assertFalse(dll.empty())

        # (4) DLL after removing all nodes
        dll.head = dll.tail = None
        dll.size = 0
        self.assertTrue(dll.empty())

    def test_push(self):

        # (1) push single node on back
        dll = DLL()
        dll.push(0)
        self.assertIs(dll.head, dll.tail)

        # (2) push single node on front
        dll = DLL()
        dll.push(0, back=False)
        self.assertIs(dll.head, dll.tail)

        # (3) push multiple nodes on back
        dll = DLL()
        lst = []
        for i in range(5):
            dll.push(i)
            lst.append(i)

        # (4) push multiple nodes on front
        dll = DLL()
        lst = []
        for i in range(5):
            dll.push(i, back=False)
            lst.insert(0, i)

    def test_pop(self):

        # (1) pop back on empty list (should do nothing)
        dll = DLL()
        try:
            dll.pop()
        except Exception as e:
            self.fail(msg=f"Raised {type(e)} when popping from back of empty list.")

        # (2) pop front on empty list (should do nothing)
        dll = DLL()
        try:
            dll.pop(back=False)
        except Exception as e:
            self.fail(msg=f"Raised {type(e)} when popping from front of empty list.")

        # (3) pop back on multiple node list
        dll = DLL()
        lst = []
        for i in range(5):  # construct list
            dll.push(i)
            lst.append(i)
        for i in range(5):  # destruct list
            dll.pop()
            lst.pop()

        # (4) pop front on multiple node list
        dll = DLL()
        lst = []
        for i in range(5):  # construct list
            dll.push(i)
            lst.append(i)
        for i in range(5):  # destruct list
            dll.pop(back=False)
            lst.pop(0)

    def test_find(self):

        # (1) find in empty DLL
        dll = DLL()
        node = dll.find(331)
        self.assertIsNone(node)

        # (2) find existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        node = dll.find(0)
        self.assertIsInstance(node, Node)
        self.assertEqual(0, node.value)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

        # (3) find non-existing value in single-node DLL
        node = dll.find(331)
        self.assertIsNone(node)

        # (4) find in longer DLL with all unique values
        dll = DLL()
        for i in range(10):
            dll.push(i)

        node = dll.find(0)
        self.assertIsInstance(node, Node)
        self.assertIs(dll.head, node)
        self.assertIsNone(node.prev)
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.next.value)

        node = dll.find(9)
        self.assertIsInstance(node, Node)
        self.assertIs(dll.tail, node)
        self.assertIsNone(node.next)
        self.assertEqual(9, node.value)
        self.assertEqual(8, node.prev.value)

        node = dll.find(4)
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)
        self.assertEqual(3, node.prev.value)
        self.assertEqual(5, node.next.value)

        node = dll.find(331)
        self.assertIsNone(node)

        # (5) find first instance in longer DLL with duplicated values
        for i in range(9, 0, -1):  # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)

        node = dll.find(0)  # should find head 0, not tail 0
        self.assertIsInstance(node, Node)
        self.assertIs(dll.head, node)
        self.assertIsNone(node.prev)
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.next.value)

        node = dll.find(9)  # should find first 9
        self.assertIsInstance(node, Node)
        self.assertEqual(9, node.value)
        self.assertEqual(8, node.prev.value)
        self.assertEqual(9, node.next.value)

        node = dll.find(4)  # should find first 4
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)
        self.assertEqual(3, node.prev.value)
        self.assertEqual(5, node.next.value)

        node = dll.find(331)
        self.assertIsNone(node)

    def test_delete(self):

        # (1) delete from empty DLL
        dll = DLL()
        result = dll.delete(331)
        self.assertFalse(result)

        # (2) delete existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        result = dll.delete(0)
        self.assertTrue(result)

        # (3) delete non-existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        result = dll.delete(331)
        self.assertFalse(result)

        # (4) delete from longer DLL with all unique values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            result = dll.delete(to_delete[i])
            self.assertTrue(result)
            result = dll.delete(331)
            self.assertFalse(result)

            lst.remove(to_delete[i])

        # (5) delete first instance in longer DLL with duplicated values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        for i in range(9, -1, -1):  # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            result = dll.delete(to_delete[i])
            self.assertTrue(result)
            result = dll.delete(331)
            self.assertFalse(result)

            lst.remove(to_delete[i])

    def test_reverse(self):

        # (1) reverse empty DLL
        dll = DLL()
        dll.reverse()

        # (2) reverse single-node DLL
        dll = DLL()
        dll.push(0)
        dll.reverse()

        # (3) reverse longer DLL
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        old_head, old_tail = dll.head, dll.tail
        dll.reverse()
        new_head, new_tail = dll.head, dll.tail
        lst.reverse()

        self.assertIs(new_head, old_tail)
        self.assertIs(new_tail, old_head)

        # (4) reverse palindrome DLL
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        for i in range(9, -1, -1):
            dll.push(i)
            lst.append(i)
        old_head, old_tail = dll.head, dll.tail
        dll.reverse()
        new_head, new_tail = dll.head, dll.tail
        lst.reverse()

        self.assertIs(new_head, old_tail)
        self.assertIs(new_tail, old_head)