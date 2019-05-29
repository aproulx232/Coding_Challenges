"""Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time."""


class StackElement:
    def __init__(self, val, next_element=None):
        self.val = val
        self.max = val
        self.next_element = next_element

    def push(self, val):
        self.next_element = StackElement(self.val, self.next_element)
        self.next_element.max = self.max
        self.val = val
        if self.next_element.max > val:
            self.max = self.next_element.max
        else:
            self.max = val

    def pop(self):
        if self is None:
            return None
        if self.next_element is not None:
            self.max = self.next_element.max
            self.val = self.next_element.val
            self.next_element = self.next_element.next_element
        else:
            self.max = None
            self.val = None
            return None

    def max_s(self):
        if self is None:
            return None
        else:
            return self.max


if __name__ == "__main__":
    stack = StackElement(2)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(3)
    print("Max: ", stack.max_s())  # 4
    stack.push(5)
    print("Max: ", stack.max_s())  # 5
    stack.pop()
    print("Max: ", stack.max_s())  # 4
    stack.pop()
    stack.pop()
    print("Max: ", stack.max_s())  # 4
    stack.pop()
    print("Max: ", stack.max_s())  # 4
    stack.pop()
    print("Max: ", stack.max_s())  # 3
    stack.pop()
    print("Max: ", stack.max_s())  # 2
    stack.pop()
    print("Max: ", stack.max_s())  # None

