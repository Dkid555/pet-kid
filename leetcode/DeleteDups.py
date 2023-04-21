"""ListNODE"""


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

    __repr__ = __str__


def deleteDuplicates( head):
    """
        :type head: ListNode
        :rtype: ListNode
        """
    if not head:
        return head
    tail = head
    while tail.next:
        current = tail.next
        if current.val == tail.val:
            tail.next = current.next
        else:
            tail = current
    return head

if __name__ == "__main__":
    ln=ListNode; l=ln(1, ln(1, ln(2, ln(3, ln(3)))))
    print(deleteDuplicates(l))