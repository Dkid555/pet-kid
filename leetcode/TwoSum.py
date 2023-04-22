"""Find sum of two numbers from list (target) and show their index (first that were finded)"""


def twoSum(nums, target):
    prevMap = {}  # - creation of dictionary {key: value}
    for i, n in enumerate(nums):  ## splits item from list on its index (i) and value (n)

        diff = target - n
        if diff in prevMap:
            return (prevMap[diff], i)  # to find in dictionary we are using it keys
        prevMap[n] = i  ## adding in dictionary new pair
    return


"""or (works longer, On^2)"""


def two_sum(lst, target):
    # nums.sort()
    # if lst[0] > target:
    #    return ""
    List = []
    for i in range(0, len(lst) - 1):
        right = len(lst) - 1
        k = target - lst[i]
        while right > i:
            if lst[right] == k:
                List.append(i)
                List.append(right)
                return List
            right -= 1

    return List


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))
    print(two_sum(nums, target))
