"""Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an intege"""


def change(lst):
    if lst == 'I':
        return 1

    if lst == 'V':
        return 5

    if lst == 'X':
        return 10

    if lst == 'L':
        return 50

    if lst == 'C':
        return 100

    if lst == 'D':
        return 500

    if lst == 'M':
        return 1000


def roman_to_integer(s):

    sm = 0

    # i = 0


    lst = []

    lst_int = []

    lst.extend(s)
    print(lst)
    for i in lst:
        lst_int.append(change(i))

    """print(lst_int)"""
    i = 0

    if len(lst_int) == 1:
        print(lst_int[0])
        exit()
        """ 
        return lst_int[0]
        """





    else:

        while i < len(lst_int):

            if (i < len(lst_int) - 1) and lst_int[i] < lst_int[i + 1]:

                sm = sm - lst_int[i]
            else:

                sm = sm + lst_int[i]

            i += 1
    return sm
if __name__=="__main__":
    s = input()
    print(roman_to_integer(s))
