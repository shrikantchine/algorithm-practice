class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_ll(head):
    curr = head
    while curr.next:
        print(f"{curr.val} -> ", end='')
        curr = curr.next
    print(curr.val)

def add(head1,  head2):
    result = None
    M, N = 0, 0
    curr = head1
    while curr:
        M += 1
        curr = curr.next
    curr = head2
    while curr:
        N += 1
        curr = curr.next
    s = min(M, N)
    result = None
    carry = 0
    final = None
    while s > 0:
        addition = head1.val + head2.val + carry
        carry = addition//10
        if not result:
            result = Node(addition%10)
            final = result
        else:
            result.next = Node(addition%10)
            result = result.next
        s -= 1
        head1 = head1.next
        head2 = head2.next
    s = min(M, N)
    remaining = head1 if head1 else head2
    while max(M, N)-s  > 0:
        addition = head1.val + head2.val + carry
        result.next = Node(addition%10)
        carry = addition//10
        s += 1
        remaining = remaining.next

    return final


head1 = Node(1, Node(2, Node(3)))
head2 = Node(4, Node(5, Node(6)))
print(add(head1, head2))