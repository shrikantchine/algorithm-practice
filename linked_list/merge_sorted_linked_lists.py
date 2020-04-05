class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


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

first = Node(5, Node(10, Node(15, Node(40))))
second = Node(2, Node(3, Node(20)))
print_ll(merge(first, second))