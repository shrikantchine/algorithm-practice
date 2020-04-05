class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detect_loop(head):
    slow, fast = head, head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(detect_loop(head))

head.next.next.next.next.next = head.next.next.next
print(detect_loop(head))