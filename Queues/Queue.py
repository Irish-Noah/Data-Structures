class Queue:
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

    def top(self):
        if not self.empty():
            return self.container[0]
        return None

    def push(self, value):
        self.container.append(value)
        self.size += 1

    def pop(self):
        if not self.empty():
            self.size -= 1
            return self.container.pop(0)
        return None