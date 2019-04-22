"""#8 [Easy]

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count(node, prev_len):
    total =0
    if node.left is not None:
        if node.left.val == node.val:
            total = total + 1 + prev_len +  count(node.left, 1 + prev_len)
        else:
            total = total + count(node.left, 0)
    if node.right is not None:
        if node.right.val == node.val:
            total = total + 1 + prev_len +  count(node.right, 1 + prev_len)
        else:
            total = total + count(node.right, 0)
    print("total: ", total)
    return total
node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
node = Node(0, Node(0), Node(0, Node(0, Node(0), Node(0)), Node(0)))
"""0
  / \
 0   0
    / \
   0   0
  / \
 0   0"""
print("count: ", count(node, 0))
