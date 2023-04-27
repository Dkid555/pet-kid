"""There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds."""

import math


def bulbSwitch(n):
    return int(math.sqrt(n))


# n = 0, 0
# n = 1, 1
# n = 2, 10
# n = 3, 100
# n = 4, 1001
# n = 5, 10010
# n = 6, 100100
# n = 7, 1001000
# n = 8, 10010000
# n = 9, 1001000001
# It seems that the i-th bulb will only remain on if i is a squared number.

"""or"""


def bulb(n):
    i = 1
    count = 0
    while i * i <= n:
        i += 1
        count += 1
    return count


if __name__ == "__main__":
    n = int(input("number of bulbs and iterations: "))
    print(bulbSwitch(n))
    print(bulb(n))
