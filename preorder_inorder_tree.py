"""Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(l):
    if len(l) == 0:
        return None
    return Node(l[0], preorder(l[1:int(len(l)/2)+1]), preorder(l[int(len(l)/2)+1:]))


def inorder(l):
    if len(l) == 0:
        return None
    return Node(l[int(len(l) / 2)], preorder(l[:int(len(l) / 2)]), preorder(l[int(len(l) / 2) + 1:]))



if __name__ == "__main__":
    root_pre = preorder(['a', 'b', 'd', 'e', 'c', 'f', 'g'])
    print("preorder: ", root_pre)
    root_in = inorder(['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    print("inorder: ", root_in)