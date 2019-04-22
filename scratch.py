


def add_to(number_list, k):
    for i in number_list:
        for j in number_list[i:]:
            if i + j == k:
                print("numbers", i, " ", j)
                return 1
    print("no numbers")
    return 0
print(add_to([1, 2, 3, 4],20))