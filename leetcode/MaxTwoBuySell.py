"""123. Best Time to Buy and Sell Stock III
Hard
8K
155
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)."""


import sys

prices = [7, 1, 5, 3, 6, 4]

def maxTwoBuySell(arr, size):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0

    for i in range(size):
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i])
        second_sell = max(second_sell, second_buy + arr[i])

    return second_sell

if __name__ == "__main__":
    print(maxTwoBuySell(prices, len(prices)))