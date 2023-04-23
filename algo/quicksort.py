def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick(arr, low, pi - 1)
        quick(arr, pi + 1, high)


if __name__ == '__main__':
    lst = [12, 34, 54, 2, 3, -1, 200, 500, -1000, 5000]
    quick(lst, 0, len(lst) - 1)
    print(lst)
