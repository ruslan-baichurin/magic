class Stack:

    def __init__(self) -> None:
        self._container = []

    def push(self, item) -> None:
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin, end, temp, n) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


num_discs = 20
tower_a = Stack()
tower_b = Stack()
tower_c = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


hanoi(tower_a, tower_c, tower_b, num_discs)
print(tower_a)
print(tower_b)
print(tower_c)