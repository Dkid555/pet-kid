"""
11 -> 2
114 -> 6
227 -> 11 -> 2
11111569 -> 25 -> 7


"""

if __name__ == "__main__":
    digit = int(input())
    if digit == 0:
        print(digit)
    else:
        print("it goes till: ", (digit - 1) % 9 + 1)
