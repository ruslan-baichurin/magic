class Queue:
    def __init__(self):
        self.items = []
        self.max_number = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def show_max_number(self):
        return self.max_number[-1]

    def enqueue(self, item):
        self.items.insert(0, item)
        if not self.max_number or item > self.max_number[-1]:
            self.max_number.append(item)

    def dequeue(self):
        if self.items:
            pop_num = self.items.pop()
            if pop_num == self.max_number[-1]:
                self.max_number.pop()
            return pop_num
        else:
            raise IndexError("The queue is empty. Can't return anything")

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(10)
q.enqueue(10)
q.enqueue(10)


print(q.size())
