class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLL:
    # Construct a SLL object
    def __init__(self):
        self.head, self.tail = None, None
        self.size = 0

    # Represent the SLL as a string
    def __repr__(self):
        result = ""
        node = self.head
        while node is not None:
            result += node.val
            if node.next is not None:
                result += "<->"
            node = node.next
        return result

    # Represent the SLL as a string
    def __str__(self):
        return repr(self)

    # Add a node to the SLL
    def add_node(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    # check if SLL is empty
    def empty(self):
        return not self.size






