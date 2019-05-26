"""The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}"""


def power_set(s):
    print(s)
    if s is None:
        return s
    out_set = []
    out_set.append(s)
    for i in s:
        ss = s.copy()
        ss.remove(i)
        out_set = out_set + power_set(ss)
    return out_set


if __name__ == "__main__":
    print(power_set([1,5,7,2,9]))