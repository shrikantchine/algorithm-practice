class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse(head, group_size):
    prev, curr, nxt = None, None, head
    count = 0
    while nxt and count < group_size:
        curr = nxt
        nxt = nxt.next
        curr.next = prev
        prev = curr
        count += 1
    if nxt is not None:
        head.next = reverse(nxt, group_size)
    return prev


def print_ll(head):
    curr = head
    while curr.next:
        print(f"{curr.val} -> ", end='')
        curr = curr.next
    print(curr.val)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(head)
print_ll(reverse(head, 2))