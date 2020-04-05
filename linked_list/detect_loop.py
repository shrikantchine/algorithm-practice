class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def detect_loop(head):
    slow, fast = head,head
    while fast:
        if fast.next is None or fast.next.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True


no_loop = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(detect_loop(no_loop))
loop = Node(1, Node(2, Node(3)))
loop.next.next.next = loop.next
print(detect_loop(loop))