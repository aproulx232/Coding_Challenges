"""Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars."""


def max_profit(l):
    max_prof = 0
    for k, b in enumerate(l):
        for s in l[k:]:
            profit = s - b
            if profit > max_prof:
                max_prof = profit
    return max_prof


if __name__ == "__main__":
    print("max profit: ", max_profit([9, 11, 8, 5, 7, 10]))
    print("max profit: ", max_profit([]))
    print("max profit: ", max_profit([10, 10]))
    print("max profit: ", max_profit([10, 8]))
    print("max profit: ", max_profit([8, 10]))
    print("max profit: ", max_profit([8, 5, 10]))