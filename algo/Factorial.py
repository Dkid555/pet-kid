import math


def Fact(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


if __name__ == "__main__":
    num = int(input())
    print("you number -", num, ", factorial is: ", Fact(num))
    # or by math package
    print("you number -", num, ", factorial is: ", math.factorial(num))
