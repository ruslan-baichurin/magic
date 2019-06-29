import operator

from data_structures.stacks import Stack


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.value

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value)

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()


def build_parse_tree(exp: str):
    exp_list = exp.split()
    parent_stack = Stack()
    parse_tree = BinaryTree('')
    parent_stack.push(parse_tree)
    current_tree = parse_tree

    for item in exp_list:
        if item == '(':
            current_tree.insert_left('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif item not in ['+', '-', '*', '/', ')']:
            current_tree.set_value(int(item))
            parent = parent_stack.pop()
            current_tree = parent
        elif item in ['+', '-', '*', '/']:
            current_tree.set_value(item)
            current_tree.insert_right('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif item == ')':
            current_tree = parent_stack.pop()
        else:
            raise ValueError("The expression doesn't seem to be correct.")
    return parse_tree


def evaluate(parse_tree: BinaryTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        oper = opers[parse_tree.get_value()]
        return oper(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_value()


# t = BinaryTree('a')
# t.insert_left('b')
# t.insert_right('c')
# t.left_child.insert_right('d')
# t.right_child.insert_left('e')
# t.right_child.insert_right('f')
# print(t.right_child.left_child, t.right_child.right_child)

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
pt.in_order()
