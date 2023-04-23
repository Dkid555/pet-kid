def shell(lst):
    size = len(lst)
    gap = size // 2
    while gap > 0:
        j = gap
        while j < len(lst):
            i = j - gap
            while i >= 0:
                if lst[i + gap] >= lst[i]:
                    break
                else:
                    lst[i], lst[i + gap] = lst[i + gap], lst[i]
                i = i - gap
            j += 1
        gap //= 2
    return lst


if __name__ == "__main__":
    lst = [12, 34, 54, 2, 3, -1, 200, 500, -1000, 5000]
    print(shell(lst))
