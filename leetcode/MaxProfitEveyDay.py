"""Max profit (you can sell on each day)"""
prices = [7, 1, 5, 3, 6, 4]


def Prof(prices):
    profit = 0
    d = len(prices)

    for i in range(1, d):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


if __name__ == "__main__":
    print(Prof(prices))
