class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add_at_end(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def reverse(self):
        if not self.head:
            return None
        prev, curr, nxt = None, None, self.head
        while nxt:
            curr = nxt
            nxt = nxt.next
            curr.next = prev
            prev = curr
        self.head = curr

    def __str__(self):
        if not self.head:
            return ""
        ret = ""
        curr = self.head
        while curr:
            ret += "{} -> ".format(curr.val)
            curr = curr.next
        return ret[:-4]


ll = LinkedList()
ll.add_at_end(2)
ll.add_at_end(3)
ll.add_at_end(4)
ll.add_at_end(5)
print(str(ll))
ll.reverse()
print(str(ll))