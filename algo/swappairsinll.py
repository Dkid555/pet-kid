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


def swapPairs(head: ListNode):
    dummy = ListNode(0, head)
    current = dummy

    while current.next != None and current.next.next != None:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return dummy.next


"""OR"""


def swap(head: ListNode):
    left = dummy = ListNode(0, head)

    while left.next and left.next.next:
        second = left.next
        third = second.next

        second.next = third.next
        third.next = second

        left.next = third
        left = second

    return dummy.next


if __name__ == "__main__":
    n2 = ListNode(0, None)
    n2.append(1)
    n2.append(2)
    n2.append(65)
    d = swap(n2)
    d.display()
    d1 = swapPairs(n2)
    d1.display()
