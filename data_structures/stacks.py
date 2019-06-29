class Stack:
    def __init__(self):
        self.items = []
        self.max_number = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

s = Stack()

s.push(5)
s.push(20)
s.push(3)
s.push(40)
s.pop()