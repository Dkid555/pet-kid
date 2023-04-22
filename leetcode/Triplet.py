"""Find all triplets in list which sum is a zero"""


def Del(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


def TripleF(lst, sum):
    lst.sort()
    # if len(lst) == 3:
    #    if lst[0]+lst[1]+lst[2] == 0:
    #       return lst
    #  else:
    #     return ""

    z = []
    List = []
    for i in range(0, len(lst) - 2):
        left = i + 1
        right = len(lst) - 1
        while left < right:
            if lst[i] + lst[left] + lst[right] == sum:
                z.append(lst[i])
                z.append(lst[left])
                z.append(lst[right])
                List.append(z)
                z = []
                right = right - 1
                left = left - 1
            if lst[i] + lst[left] + lst[right] < sum:
                left = left + 1
            else:
                right = right - 1
    return Del(List)


lst = [1, 3, 4, 5, 6, -4, -2]
if __name__ == "__main__":
    print(TripleF(lst, 0))
