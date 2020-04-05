class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def kth_last_node(head, k):
    slow, fast = head, head
    while fast is not None and k > 0:
        fast = fast.next
        k -= 1
    if not fast:
        return -1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.val

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(kth_last_node(head, 2))