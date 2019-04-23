"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?


[0, 1, 4, 5, 0, -2, 4, 1] => 1 5 4 => 10
[1, 2, 1, 2, 1, 2,  50, 2] => 54
"""


def sum_adj(l):
    odd = 0
    even = 0
    for i in l:
        temp = odd
        odd = even + i
        even = max(temp, even)
    return max(odd, even)


print(sum_adj([2, 4, 6, 2, 5]))  # 13
print(sum_adj([0, 1, 4, 5, 0, -2, 4, 1]))  # 10
print(sum_adj([1, 2, 1, 2, 1, 2,  50, 2]))  # 54
