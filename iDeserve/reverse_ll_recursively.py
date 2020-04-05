class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse(head):
    prev = None
    curr = None
    nxt = head
    while nxt:
        prev = curr
        curr = nxt
        nxt = nxt.next
        curr.next = prev
    
    x = curr
    while x.next:
        print(x.data, end=' -> ')
        x = x.next
    print(x.data)


head = Node(1, Node(2, Node(3, Node(4))))
reverse(head)