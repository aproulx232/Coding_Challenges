"""Given the root to a binary search tree, find the second largest node in the tree."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def second_largest(node):
    largest, second = _second_largest(node)
    return second


def _second_largest(node, largest=None, second=None):
    if largest is None or node.val > largest:
        second = largest
        largest = node.val
    elif node.val > second:
        second = node.val
    if node.left is not None:
        largest, second = _second_largest(node.left, largest, second)
    if node.right is not None:
        largest, second = _second_largest(node.right, largest, second)
    return largest, second



if __name__ == "__main__":
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(3)), Node(4)))
    print(second_largest(node))
    node = Node(0, Node(5), Node(0, Node(1, Node(1), Node(3)), Node(4)))
    print(second_largest(node))
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(4)))
    print(second_largest(node))
