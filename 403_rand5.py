import random


def rand5():
    return random.randint(1, 5)


def rand7():
    rand25 = 5 * (rand5() - 1) + rand5()
    if rand25 > 7:
        return rand7()
    else:
        return rand25


dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for x in range(1000000):
    num = rand7()
    dist.update({num: dist[num] + 1})
print(dist)
