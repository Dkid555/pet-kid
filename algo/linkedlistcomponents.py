"""You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, Value):
        if self == None:
            print("Error, no data in list")
            return
        while self.next != None:
            self = self.next
        a = ListNode(Value, None)
        self.next = a

    def display(self):
        s = " "
        while self != None:
            s = s + str(self.val) + " "
            self = self.next
        print(s)


def numComponents(head, nums):
    c, p, nums = 0, False, set(nums)
    while head:
        if head.val in nums and not p:
            c += 1
        p = head.val in nums
        head = head.next
    return c

    #
    # return head


if __name__ == "__main__":
    n1 = ListNode(0, None)
    n1.append(1)
    n1.append(2)
    n1.append(3)
    n1.append(4)
    n1.append(5)
    n1.append(9)
    n1.append(10)
    nums = [0, 3, 1, 9, 10, 14, 15]
    print(numComponents(n1, nums))
