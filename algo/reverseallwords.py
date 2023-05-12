def revers(s):
    s = s.split()
    l = []
    for i in s:
        l.append(i[::-1])
    return l


if __name__ == "__main__":
    s = input()
    print(" ".join(revers(s)))
