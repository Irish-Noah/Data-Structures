class Stack:
    # construct an empty stack
    def __init__(self):
        self.container = []
        self.size = 0

    # represent a stack as a string
    def __str__(self):
        it = 0
        rep = ""
        while it < self.size:
            rep += self.container[it]
            if it == self.size-1:
                rep += "<->"

    # represent a stack as as string
    def __repr__(self):
        str(self)

    def empty(self):
        return not self.size

    # return the top stack if not empty
    def top(self):
        if not self.empty():
            return self.container[-1]
        return None

    # add new elem to stack
    def push(self, val):
        self.container.append(val)
        self.size += 1

    # pop top elem and return it
    def pop(self):
        if not self.empty():
            self.size -= 1
            return self.container.pop()


