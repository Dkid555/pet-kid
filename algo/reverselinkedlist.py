"""class node:
    def __init__(self, data=None):
        self.data = data  ## - data that are stored
        self.next = None  ## key to the next element


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def len(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur = self.head
        elem = []
        while cur.next != None:
            # print(cur.data)
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def get(self, index):
        if (index > self.len()):
            return ("Error: There is no such element/Index out of range")

        else:
            cur = self.head
            for i in range(0, index + 1):
                cur = cur.next
            return cur.data

    def erase(self, index):
        if index >= self.len():
            print("Error: There is no such element/Index out of range")
            return
        i = 0
        cur = self.head
        while True:
            # if i == index:
            # return
            last_node = cur
            cur = cur.next
            if i == index:
                last_node.next = cur.next
                return
            i += 1

    def reverse(self):
        prev = None
        cur = self.head
        #cur = cur.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            print(prev.data)
            cur = next
        self.head = prev




if __name__ == "__main__":
    new = linked_list()
    new.append(12)
    new.append(1)
    new.append(2)
    new.append(3)
    #new.display()
    #new.erase(3)
    new.display()
    new.reverse()
    #new.reverse()
    new.display()
"""

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            # rint(prev.data)
            cur = next

        return prev



"""

"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        tail = self.next and f', {self.next}' or ''
        return f'{self.val!r}{tail}'

    def __next__(self):
        if self.next:
            return self.next
        raise StopIteration

    def __iter__(self):
        item = self
        while item:
            yield item.val
            item = item.next

    def copy(self):
        return ListNode(self.val, self.next and self.next.copy())

    def display(self):
        cur = self
        g = []
        while cur != None:
            cur =  cur.next
            g.append(cur.val)
        return g

    def reverse(self):
        prev = None
        cur = self
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            # rint(prev.data)
            cur = next

        return prev




if __name__ == "__main__":
    ll = ListNode(1)
    ll = ListNode(2)
    ll.reverse()
    print(ll.display())
"""


class node:
    def __init__(self, data=None):
        self.data = data  ## - data that are stored
        self.next = None  ## key to the next element


# class linked_list:
#     def __init__(self):
#         self.head = node()
#
#     def append(self, data):
#         new_node = node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
#
#     def display(self):
#         cur = self.head
#         g = []
#         while cur.next != None:
#             cur = cur.next
#             g.append(cur.data)
#         print(g)
#     """def display(self):
#         cur = self.head
#         elem = []
#         while cur.next != None:
#             # print(cur.data)
#             cur = cur.next
#             elem.append(cur.data)
#         print(elem)"""
#     def lenght(self):
#         i = 0
#         cur = self.head
#         while cur.next != None:
#             i += 1
#             cur = cur.next
#         return i
#     def get(self, index):
#         if index > self.lenght() - 1:
#             return "Error"
#         cur = self.head
#         cur = cur.next
#         for i in range (0, index):
#             cur = cur.next
#         return cur.data
#
#     def pop(self, index):
#         if index > self.lenght() - 1:
#             return "Error"
#         i = 0
#         cur = self.head
#         while True:
#             # if i == index:
#             # return
#             last_node = cur
#             cur = cur.next
#             if i == index:
#                 last_node.next = cur.next
#                 return
#             i += 1
#     def reverse(self):
#         #prev = None
#         cur = self.head
#         rev = linked_list()
#         g = []
#         while cur.next != None:
#             #prev = cur
#             cur = cur.next
#             g.append(cur.data)
#         cur = self.head
#         #cur = cur.next
#         for i in g[::-1]:
#             cur = cur.next
#             cur.data = i

def rev_On(head: node):
    if head == None or head.next == None:
        return head
    temp = None
    rev = None
    while head != None:
        print(head.data)
        temp = head
        head = head.next
        temp.next = rev
        rev = temp
    return rev


def rev_rec(head: node, i):
    if head == None or head.next == None:
        return head
    i += 1
    print(i)
    rec = rev_rec(head.next, i)
    head.next.next = head
    head.next = None
    return rec


def print_list(head: node):
    temp = head
    s = ""
    while temp != None:
        s = s + (str(temp.data) + " ")
        temp = temp.next
    print(s)


def r(head: node):
    if head == None or head.next == None:
        return head
    temp = None
    ref = None
    while head != None:
        temp = head
        head = head.next
        temp.next = ref
        ref = temp
    return ref


def r1(head: node):
    if head == None of head.next == None:
        return head
    rec = r1(head.next)
    head.next.next = head
    head.next = None
    return rec


def r_O1(head: node):
    if head == None or head.next == None:
        return head
    rec = r_O1(head.next)
    head.next.next = head
    head.next = None
    return rec


def rev(head: node):
    if head == None or head.next == None:
        return head
    rec = rev(head.next)
    head.next.next = head
    head.next = None
    return rec


def rev_w(head: node):
    if head == None or head.next == None:
        return head
    temp = None
    ref = None
    while head != None:
        temp = head
        head = head.next
        temp.next = ref
        ref = temp

    return ref


if __name__ == "__main__":
    n1 = node(12)
    n2 = node(1)
    n3 = node(2)
    n4 = node(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    print_list(n1)
    # n = rev_On(n1)
    n = r_O1(n1)
    # n = r(n1)
    print("=====")
    print_list(n)
