class Node(object):
    def __init__(self, val, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom


def flatten(head):
    if not head:
        return None
    if head.next is None and head.bottom is None:
        return head.val
    next_sorted = flatten(head.next)
    bottom_sorted = flatten(head.bottom)
    return merge(next_sorted, bottom_sorted)

def merge(first, second):
    result = first if first.val < second.val else second
    other = first if first.val >= second.val else second
    head = result
    while other:
        if result.next is None:
            result.next = other
            break
        if result.next.val > other.val:
            tmp = result.next
            result.next = other
            other = tmp
        else:
            result = result.next

    return head


def print_ll(head):
    curr = head
    while curr.next:
        print(f"{curr.val} -> ", end='')
        curr = curr.next
    print(curr.val)

head = Node(5, next=Node(10, next=Node(19, next=Node(28))))
head.bottom = Node(7, bottom=Node(8, bottom=Node(30)))
head.next.bottom = Node(20)
head.next.next.bottom = Node(22, bottom=Node(50))
head.next.next.next.bottom = Node(35, bottom=Node(40, bottom=Node(45)))

print_ll(flatten(head))