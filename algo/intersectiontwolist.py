def intersect(lst1, lst2):
    return list(set(lst1) & set(lst2))  # & checks by bits
    # for example 14 & 4 -> 4 00000100 & 00001110 = 00000100


"""OR"""


def intersect2(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


if __name__ == "__main__":
    lst1 = [0, 1, 2, 3, 4, 5, 7]
    lst2 = [1, 7, 9, 8, 5]
    print(intersect(lst1, lst2))
    print(intersect2(lst1, lst2))
