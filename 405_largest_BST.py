

class node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "({left}, {val}, {right})".format(left=self.left, right=self.right, val=self.val)


def inOrderTraversal(tree) -> list:
    inOrderList = []
    if tree.left is None and tree.right is None:
        return [tree.val]
    if tree.left is not None:
        inOrderList += inOrderTraversal(tree.left)
    inOrderList.append(tree.val)
    if tree.right is not None:
        inOrderList += inOrderTraversal(tree.right)
    return inOrderList


def isSorted(array:list) -> bool:

    if len(array) < 2:
        return True
    for index in range(1,len(array)):
        if array[index - 1] > array[index]:
            return False
    return True


def isBST(tree) -> bool:
    arr = inOrderTraversal(tree)
    if isSorted(arr):
        return True
    return False


def sizeBST(tree) -> int:
    size = 1
    if tree.left is None and tree.right is None:
        return size
    if tree.left is not None:
        size += sizeBST(tree.left)
    if tree.right is not None:
        size += sizeBST(tree.right)
    return size


def maxSizeBST(tree) -> int:
    maxSize = 0
    if tree.left is None and tree.right is None:
        if isBST(tree):
            size = sizeBST(tree)
            maxSize = size if size > maxSize else maxSize
    if tree.left is not None:
        size = maxSizeBST(tree.left)
        maxSize = size if size > maxSize else maxSize
    if tree.right is not None:
        size = maxSizeBST(tree.right)
        maxSize = size if size > maxSize else maxSize
    if isBST(tree):
        size = sizeBST(tree)
        maxSize = size if size > maxSize else maxSize
    return maxSize


tree_6 = node(left=node(val=10, left=node(val=5),
                        right=node(val=15)), val=20, right=node(val=30))
print(tree_6)


tree_1 = node(20)
assert(sizeBST(tree_1) == 1)
assert(isBST(tree_1) == True)
assert(maxSizeBST(tree_1) == 1)

tree_2 = node(20, left=node(10))
assert(sizeBST(tree_2) == 2)
assert(isBST(tree_2) == True)
assert(maxSizeBST(tree_2) == 2)

tree_2 = node(20, left=node(30))
assert(sizeBST(tree_2) == 2)
assert(isBST(tree_2) == False)
assert(maxSizeBST(tree_2) == 1)

tree_2 = node(20, right=node(10))
assert(sizeBST(tree_2) == 2)
assert(isBST(tree_2) == False)
assert(maxSizeBST(tree_2) == 1)

tree_3 = node(20, left=node(10), right=node(30))
assert(sizeBST(tree_3) == 3)
assert(isBST(tree_3) == True)
assert(maxSizeBST(tree_3) == 3)

tree_4 = node(20, left=node(10), right=node(30, left=node(40)))
assert(sizeBST(tree_4) == 4)
assert(isBST(tree_4) == False)
assert(maxSizeBST(tree_4) == 1)

tree_5 = node(20, left=node(10), right=node(30, left=node(5)))
assert(sizeBST(tree_5) == 4)
assert(isBST(tree_5) == False)
assert(maxSizeBST(tree_5) == 2)
