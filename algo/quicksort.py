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
    arr = [10, 7, 8, 9, 1, 5, 5, 7]
    quick(arr, 0, len(arr) - 1)
    print(arr)
