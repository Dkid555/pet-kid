"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 """


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


def sum_up_two_reversed_numbers(head1: ListNode, head2: ListNode):
    temp = 0
    while head1 != None and head2 != None:
        # if head1.val != None and head2.val != None:
        head1.val = head1.val + head2.val + temp
        temp = 0
        if head1.val >= 10:
            temp = 1
            head1.val = head1.val - 10

        if head1.next == None and head2.next == None and temp == 1:
            a = ListNode(1, None)
            head1.next = a
            temp = 0

        if head1.next == None and head2.next != None:
            head1.next = head2.next
            head1 = head1.next
            break

        head1 = head1.next
        head2 = head2.next

    while head1 is not None:
        if temp == 1:
            head1.val = head1.val + 1
            temp = 0
            if head1.val >= 10:
                temp = 1
                head1.val -= 10
                if head1.next == None:
                    a = ListNode(0, None)
                    head1.next = a
        head1 = head1.next


if __name__ == "__main__":
    n1 = ListNode(8, None)
    n1.append(3)
    n1.append(6)

    n1.display()
    n2 = ListNode(5, None)
    n2.append(6)
    n2.append(4)
    n2.append(9)
    n2.display()
    sum_up_two_reversed_numbers(n1, n2)
    n1.display()

    o1 = ListNode(5, None)
    o2 = ListNode(5, None)
    sum_up_two_reversed_numbers(o1, o2)
    o1.display()
