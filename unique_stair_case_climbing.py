"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time."""


def climb_n_stairs(n):
    total = 0
    if n == 1:
        return 1
    elif n == 2:
        total = total + 1 + climb_n_stairs(n-1)
    else:
        total = total + climb_n_stairs(n-1) + climb_n_stairs(n-2)
    return total


def climb_n_stairs_x_steps(n, x):
    total = 0
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif n in x:
        total = total + 1 + sum([climb_n_stairs_x_steps(n - i, x) for i in x])
    else:
        total = total + sum([climb_n_stairs_x_steps(n - i, x) for i in x])
    return total


if __name__ == '__main__':
    print("{1,2} steps: 4 stairs: ", climb_n_stairs(4))
    print("{1, 2, 3} steps: 4 stairs: ", climb_n_stairs_x_steps(4, {1, 2, 3}))
    print("{1, 2, 3, 4,} steps: 10 stairs: ", climb_n_stairs_x_steps(10, {1, 2, 3, 4}))



