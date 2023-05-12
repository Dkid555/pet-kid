def findRest(list1, list2):
    d = {}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                d[list1[i]] = i + j
    lst = []
    for j in d.keys():
        if d[j] == min(d.values()):
            lst.append(j)
    return lst


"""OR"""


def findRest_On(list1, list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = i
        min_val = 2000
        SUM = 0
        res = []
    for j in range(len(list2)):
        if list2[j] in d:
            SUM = j + d[list2[j]]
            if SUM < min_val:
                res.clear()
                res.append(list2[j])
                min_val = SUM
            elif SUM == min_val:
                res.append(list2[j])
    return res


if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    print(findRest(list1, list2))
    print(findRest_On(list1, list2))
