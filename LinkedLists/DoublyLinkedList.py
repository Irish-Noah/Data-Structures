from typing import TypeVar, List


T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)

class Node:

    __slots__ = ["value", "next", "prev"]

    # construct a node
    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        self.next = next
        self.prev = prev
        self.value = value

    # represent the node as a string
    def __repr__(self) -> str:
        return str(self.value)

    # represent the node as a string
    def __str__(self) -> str:
        return str(self.value)


class DLL:

    __slots__ = ["head", "tail", "size"]

    # construct an empty DLL
    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    # represent the DLL as string
    def __repr__(self) -> str:
        result = ""
        node = self.head
        while node is not None:
            result += str(node)
            if node.next is not None:
                result += " <-> "
            node = node.next
        return result

    # represent the DLL as a string
    def __str__(self) -> str:
        return repr(self)

    # check if the DLL is empty
    def empty(self) -> bool:
        return not self.size

    # add a new node to the DLL
    def push(self, val: T, back: bool = True) -> None:
        new_node = Node(val)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        elif back:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        # "And again, it just works" - Todd "The god" Howard

    # Remove Node from back (or front) of DLL
    def pop(self, back: bool = True) -> None:
        if self.empty():
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            if back:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.head.next
                self.head.prev = None
        self.size -= 1
        # "If you do the thing, and you don't mess it up... It works, it just works" - Jontron

    # Find first instance of val in the DLL and return associated Node object.
    def find(self, val: T) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Delete first instance of `val` in the DLL.
    def delete(self, val: T) -> bool:
        node = self.head
        while node is not None:
            if node.value == val:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                    self.size -= 1
                else:
                    if node.next is None:
                        self.pop(True)
                    elif node.prev is None:
                        self.pop(False)
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        self.size -= 1
                return True
            node = node.next
        return False

    # Reverse DLL in-place
    def reverse(self) -> None:
        node = self.head
        temp_node = None
        while node is not None:
            temp_node = node.prev
            node.prev = node.next
            node.next = temp_node
            node = node.prev
        if temp_node is not None:
            self.tail = self.head
            self.head = temp_node.prev
