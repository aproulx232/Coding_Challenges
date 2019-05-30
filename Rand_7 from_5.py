"""Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive)."""

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    x = rand10()
    while x > 7:
        x = rand10()
    return x


def rand10():
    rand10 = None
    i = rand5()
    while i > 2:
        i = rand5()
    if i == 1:
        rand10 = rand5()
    else:
        rand10 = 5 + rand5()
    return rand10


if __name__ == "__main__":
    #print(rand7())
    rand_list = []
    for i in range(100000):
        rand_list.append(rand7())
    rand_list.sort()
    print(sum(rand_list) / len(rand_list))