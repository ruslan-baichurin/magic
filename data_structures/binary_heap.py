class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __str__(self):
        return str(self.heap_list)

    def swap_items(self, ind1, ind2):

        self.heap_list[ind1], self.heap_list[ind2] = self.heap_list[ind2], self.heap_list[ind1]

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.swap_items(index, index // 2)
            index //= 2

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            min_child_ind = self.min_child(index)

            if self.heap_list[index] > self.heap_list[min_child_ind]:
                self.swap_items(index, min_child_ind)

            index = min_child_ind

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)

        return min_val

    def build_heap(self, lst):
        index = len(lst) // 2
        self.current_size = len(lst)
        self.heap_list = [0] + lst[:]
        while index > 0:
            self.perc_down(index)
            index -= 1



bh = BinaryHeap()
my_list = [9, 6, 5, 2, 3]
bh.build_heap(my_list)
print(bh)


