def Fibo(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    l = [0, 1]
    k = 0
    for i in range(1, num + 1):
        key = l[i - 1] + l[i]
        if key >= num:
            if key == num:
                l.append(key)
            return l
        l.append(key)
        # k = i


if __name__ == "__main__":
    num = int(input())

    print(Fibo(num))
