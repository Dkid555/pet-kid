def bubble(lst):
    # i = 0
    for i in range(0, len(lst)):
        f = 0
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                f += 1
        if f == 0:
            break
    return lst


if __name__ == "__main__":
    lst = [12, 34, 54, 2, 3, -1, 200, 500, -1000, 5000]
    print(bubble(lst))
