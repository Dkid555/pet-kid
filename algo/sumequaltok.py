from collections import deque

if __name__ == "__main__":
    g = deque([-6, -5, 0, 1, 2, 3, 4, 5, 7, 10, 15])
    k = int(input("input k "))
    while g:
        i = g[0]
        g.popleft(
            delta=k - i
        if delta in g:
            print(i, delta)
        break

if __name__ == "__main__":
    g = [-6, -5, 0, 1, 2, 3, 4, 5, 7, 10, 15]
    k = int(input("input k "))
    while g:
        i = g.pop()
        delta = k - i
        if delta in g:
            print(i, delta)
            break

if __name__ == "__main__":
    g = [-6, -5, 0, 1, 2, 3, 4, 5, 7, 10, 15]
    k = int(input("input k "))
    for i in range(0, len(g)):
        delta = k - g[i]
        j = i + 1
        end = len(g) - 1
        while j <= end:
            mid = int(j + (end - j) / 2)
            if g[mid] == delta:
                print(g[i], g[mid])
                break
            if delta < g[mid]:
                end = mid - 1
            else:
                j = mid + 1

"""binary seacrh, On"""
if __name__ == "__main__":  # find equal to k
    g = [-6, -5, 0, 1, 2, 3, 4, 5, 7, 10, 15]
    k = int(input("input k "))
    i = 0
    j = len(g) - 1
    while i < j:
        sum = g[i] + g[j]
        if sum > k:
            j -= 1
        elif sum < k:
            i += 1
        else:
            print(g[i], g[j])
            break

""""""""

if __name__ == "__main__":  # find closer to k
    g = [-6, -5, 0, 1, 2, 3, 4, 5, 7, 10, 15]
    a = list()
    k = int(input("input k: "))
    i = 0
    j = len(g) - 1
    mas = 0
    z = k
    while i < j:
        sum = g[i] + g[j]
        if sum == delta:
            print(g[i], g[j])
            break
        if sum > k:
            if (z > k - sum):
                z = k - sum
                a = []
                a.append(g[i])
                a.append(g[j])
            j -= 1
        if sum < k:
            if (z > k - sum):
                z = k - sum
                a = []
                a.append(g[i])
                a.append(g[j])

            i += 1
    # if a is not None:
    print(a)
