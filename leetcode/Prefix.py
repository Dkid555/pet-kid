"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


def prefix(a):
    if len(a) == 1:
        return a[0]

    if len(a) == 0:
        return ""

    a.sort()

    size = len(a)

    end = min(len(a[0]), len(a[size - 1]))
    i = 0
    # print(end)

    while (i < end and a[0][i] == a[size - 1][i]):
        i += 1

    return a[0][0: i]


strs = ["cars", "cargurus", "car"]
if __name__ == "__main__":
    print(prefix(strs))
