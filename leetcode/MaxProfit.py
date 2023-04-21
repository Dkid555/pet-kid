"""Max profit (find one best day to buy and one to sell)"""

import sys

prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
    maxprof = 0
    min_pr = sys.maxsize
    for i in range(0, len(prices)):
        if (min_pr > prices[i]):
            min_pr = prices[i]
        elif (prices[i] - min_pr > maxprof):
            maxprof = prices[i] - min_pr

    return maxprof

if __name__ == "__main__":
    print(maxProfit(prices))
