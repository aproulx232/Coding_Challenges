"""Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24."""


def sum_to(l, k):
    ls = []
    for i in l:
        if i <= k:
            ls.append(i)
    return _sum_to(ls, k, 0)

def _sum_to(l, k, s):
    if len(l) == 0:
        return None
    elif l[0] + s < k:
        x = _sum_to(l[1:], k, l[0] + s)
        if x is None:
            return _sum_to(l[1:], k, s)
        else:
            return [l[0]] + x
    elif l[0] + s > k:
        return _sum_to(l[1:], k, s)
    else:
        return [l[0]]


if __name__ == "__main__":
    print(sum_to([12, 1, 61, 5, 9, 2], 24))