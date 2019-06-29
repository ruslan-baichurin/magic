class Node:
    def __init__(self, data):
        """Constructor to initiate the object"""

        # store data
        self.data = data

        # store reference to the next item
        self.next_node = None

        # store reference to the previous item
        self.previous_node = None

    def has_value(self, value):
        """Method to compare the value with the node data"""

        return self.data == value


class SinglyLinkedList:
    def __init__(self):
        """Constructor to initiate the object"""

        self.head = None
        self.tail = None

    def add_node(self, item):
        """Method to add a node at the end of the list"""

        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next_node = item

        self.tail = item

    def list_length(self):
        """Method to return the number of list items"""

        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1

            current_node = current_node.next_node

        return count

    def output_list(self):
        current_node = self.head
        out = ''

        while current_node is not None:
            out += str(current_node.data) + ' -> '

            current_node = current_node.next_node
        print(out[:-4])

    def unordered_search(self, value):
        """Method to return a list of nodes that have the input value"""

        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next_node
            node_id += 1

        return results

    def remove_item_by_id(self, id):
        """Method to remove an item with the input id"""

        current_id = 1
        current_node = self.head
        prev_node = None

        while current_node is not None:
            if current_id == id:
                if prev_node is not None:
                    prev_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node

                return

            prev_node = current_node
            current_node = current_node.next_node
            current_id += 1

        return


class DoublyLinkedList:
    def __init__(self):
        """Constructor to initiate the object"""

        self.head = None
        self.tail = None

    def add_node(self, item):
        """Method to add a node at the end of the list"""

        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
            item.previous_node = None
            item.next_node = None
        else:
            self.tail.next_node = item
            item.previous_node = self.tail
        self.tail = item

        return

    def remove_item_by_id(self, item_id):
        """Method to remove an item with the input id"""

        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous_node
            next_node = current_node.next_node

            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next_node = next_node
                    if next_node is not None:
                        next_node.previous_node = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous_node = None

                return

            current_node = next_node
            current_id += 1

        return

    def list_length(self):
        """Method to return the number of list items"""

        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next_node

        return count

    def output_list(self):
        current_node = self.head
        out = ''

        while current_node is not None:
            out += str(current_node.data) + ' -> '
            current_node = current_node.next_node

        print(out[:-4])

    def unordered_search(self, value):
        """Method to return a list of nodes that have the input value"""

        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next_node
            node_id += 1

        return results


def circular(node):
    nodes = set()

    while node is not None:
        if node.next_node in nodes:
            return True
        else:
            nodes.add(node)
            node = node.next_node

    return False

sll = SinglyLinkedList()

sll.add_node(10)
sll.add_node(20)
sll.add_node(10)
sll.add_node('New York')
sll.output_list()
print(sll.list_length())
print(sll.unordered_search(10))
sll.remove_item_by_id(3)
sll.output_list()


dll = DoublyLinkedList()

dll.add_node(10)
dll.add_node(20)
dll.add_node(10)
dll.add_node('New York')
dll.output_list()
