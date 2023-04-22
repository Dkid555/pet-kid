"""Rotate numbers in list in k positions"""

from collections import deque

head = [1, 2, 3, 4, 5]
k = 3


def Rotate(head, k):
    head = deque(head)
    i = 0
    while i < k:
        z = head.pop()
        head.appendleft(z)
        i += 1
    return head


if __name__ == "__main__":
    print(Rotate(head, k))
