""" Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, value):
        if self == None:
            print("Error")
        else:
            node = ListNode(value)
            while self.next != None:
                self = self.next

            self.next = node

    def display(self):
        s = " "
        while self != None:
            s = s + str(self.val) + " "
            self = self.next
        print(s)

    def pop(self):
        while self.next.next != None:
            self = self.next
        self.next = None

    def helper(self, head, index):
        if head == None:
            return (None, 0)
        else:
            (chain, location) = self.helper(head.next, index)
            location += 1
            if location == index:
                return (chain, location)
            else:
                return (ListNode(head.val, chain), location)

    def removeNthFromEnd(self, head, index):
        (head, location) = self.helper(head, index)
        return head


if __name__ == "__main__":
    n1 = ListNode(1)
    n1.append(2)
    n1.append(3)
    n1.display()
    # n1.pop()
    n1.append(5)
    n1.append(6)
    n1.append(7)
    n1.append(8)
    n1.display()

    n1 = n1.removeNthFromEnd(n1, 2)
    n1.display()
