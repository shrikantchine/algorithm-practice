class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def find_intersection(head1, head2):
    len_head1 = 0
    len_head2 = 0
    curr = head1
    while curr:
        curr = curr.next
        len_head1 += 1
    curr = head2
    while curr:
        curr = curr.next
        len_head2 += 1
    bigger = head1 if len_head1 > len_head2 else head2
    smaller = head1 if len_head1 <= len_head2 else head2
    counter = abs(len_head1-len_head2)
    while counter > 0:
        bigger = bigger.next
        counter -= 1
    while bigger != smaller:
        bigger = bigger.next
        smaller = smaller.next

    return bigger.val


from_intersect = Node(15, Node(30))
head1 = Node(3, Node(6, Node(9, from_intersect)))
head2 = Node(10, from_intersect)
print(find_intersection(head1, head2))