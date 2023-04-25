def reverse(s):
    for i in range(0, int(len(s) / 2)):
        # print(i)
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
    return s


if __name__ == '__main__':
    s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"]

    print(reverse(s) == ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a", " ", ",", "n", "a",
                         "l", "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"])
