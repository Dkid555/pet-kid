"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

def reverse(x):
    max = 2**31 - 1
    min = -2**31

    x_str = str(x) if x >= 0 else str(x)[1:]
    x_reverse = int(x_str[::-1] if x >= 0 else '-'+  x_str[::-1])
    type(x_reverse)
    if x_reverse in range(min, max + 1):
        return x_reverse
    return 0

"""OR"""
def reverse1(x):
    rever = int(str(abs(x))[::-1])
    return (rever if x >= 0 else -rever) if rever.bit_length() < 32 else 0

if __name__== "__main__":
    x = int(input())
    print(reverse(x))
