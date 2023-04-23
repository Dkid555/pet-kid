##insert sort -  picking the element and comining it with the previous one


"""
def insertsort_1(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if (arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr
"""


def insertsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    # arr = [1]
    # arr = [12, 11, 13, 5, 6]
    arr = [-1000, 1000, -123, 7, 8, 10, 5000, 11, 2, 3, -10, 5, 6, 7, 7]
    # print(insertsort_1(arr))
    print(insertsort(arr))
