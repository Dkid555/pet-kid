class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, value):
        if self == None:
            print("Error, no data in list")
            return
        while self.next != None:
            self = self.next
        a = ListNode(value, None)
        self.next = a

    def display(self):
        s = " "
        while self != None:
            s = s + str(self.val) + " "
            self = self.next
        print(s)


def getIntersectionNode(headA, headB):
    one = headA
    two = headB

    while one != two:
        one = headB if one is None else one.next
        two = headA if two is None else two.next
    return one


if __name__ == "__main__":
    headA = ListNode(1)
    headA.append(2)
    headA.append(6)
    headB = ListNode(7)
    headB.append(8)
    headB.next.next = headA.next
    headB.display()
    getIntersectionNode(headA, headB).display()
