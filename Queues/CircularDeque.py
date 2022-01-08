from __future__ import annotations
from typing import TypeVar, List

t = TypeVar("T")                                # represents generic type
CircularDeque = TypeVar("CircularDeque")        # represents a CircularDeque object


class CircularDeque:

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    # Construct an instance of a CircularDeque
    def __init__(self, data: List[t] = [], capacity: int = 4):
        self.capacity: int = capacity
        self.size: int = len(data)

        self.queue: list(t) = [None] * capacity
        self.front: int = None
        self.back: int = None

        for index, value in enumerate(data):
            self.queue[index] = value
            self.front = 0
            self.back = index

    # Provides a string representation of a CircularDeque
    def __str__(self) -> str:

        if self.size == 0:
            return "CircularDeque <empty>"

        string = f"CircularDeque <{self.queue[self.front]}"
        current_index = self.front + 1 % self.capacity
        while current_index <= self.back:
            string += f", {self.queue[current_index]}"
            current_index = (current_index + 1) % self.capacity
        return string + ">"

    # Provides a string representation of a CircularDeque
    def __repr__(self) -> str:
        return str(self)

    # Get the length of the deque
    def __len__(self) -> int:
        return self.size

    # check if the deque is empty
    def is_empty(self) -> bool:
        return not self.size

    # get the front element of the deque
    def front_element(self) -> t:
        if not self.is_empty():
            return self.queue[self.front]

    # get the back element of the deque
    def back_element(self) -> t:
        if not self.is_empty():
            return self.queue[self.back]

    # Function that adds a given value to the front of the deque
    def front_enqueue(self, value: t) -> None:
        if self.is_empty():
            self.front = self.back = 0

        self.front = (self.front - 1) % len(self.queue)
        self.queue[self.front] = value
        self.size += 1

        if self.size == 1:
            self.back = self.front

        if self.capacity == self.size:
            self.grow()

    # Function that adds a given value to the back of the deque
    def back_enqueue(self, value: t) -> None:
        if self.is_empty():
            self.front = self.back = 0

        self.back = (self.back + 1) % len(self.queue)
        self.queue[self.back] = value
        self.size += 1

        if self.size == 1:
            self.front = self.back

        if self.capacity == self.size:
            self.grow()

    # Function that removes the front element from the deque
    def front_dequeue(self) -> t:
        if self.is_empty():
            return None
        ret = self.front_element()
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1

        if self.size <= self.capacity/4 and self.capacity/2 >= 4:
            self.shrink()

        return ret

    # Function that removes the back element from the deque
    def back_dequeue(self) -> t:
        if self.is_empty():
            return None
        ret = self.back_element()
        self.queue[self.back] = None
        self.back = (self.back - 1) % len(self.queue)
        self.size -= 1

        if self.size <= self.capacity/4 and self.capacity/2 >= 4:
            self.shrink()

        return ret

    # Function that doubles the capacity of the deque
    def grow(self) -> None:
        temp = self.queue
        ind = self.front
        self.queue = [None] * (self.capacity * 2)
        for elem in range(self.size):
            self.queue[elem] = temp[ind]
            ind = (1 + ind) % len(temp)

        self.capacity = len(self.queue)
        self.front = 0
        self.back = self.size - 1

    # Function that halves the capacity of the deque
    def shrink(self) -> None:
        temp = self.queue
        ind = self.front
        self.queue = [None] * (self.capacity // 2)
        for elem in range(self.size):
            self.queue[elem] = temp[ind]
            ind = (1 + ind) % len(temp)

        self.capacity = len(self.queue)
        self.front = 0
        self.back = self.size - 1
