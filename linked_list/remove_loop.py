class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_loop(head):
    slow, fast = head,head
    while fast:
        if fast.next is None or fast.next.next is None:
            break
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow.next = None
            break
    return head

def print_ll(head):
    curr = head
    while curr.next:
        print(f"{curr.val} -> ", end='')
        curr = curr.next
    print(curr.val)

loop = Node(1, Node(2, Node(3)))
loop.next.next.next = loop.next
print_ll(remove_loop(loop))