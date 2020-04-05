class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_intersecting_node(head1, head2):
    n, m = 0, 0
    curr = head1
    while curr:
        n += 1
        curr = curr.next

    curr = head2
    while curr:
        m += 1
        curr = curr.next

    bigger = head1 if n > m else head2
    smaller = head1 if n <= m else head2

    for _ in range(abs(m-n)):
        bigger = bigger.next
    
    while bigger and smaller and bigger != smaller:
        bigger = bigger.next
        smaller = smaller.next

    print(bigger.data)



common = Node(8, Node(9, Node(10)))
ll1 = Node(1, Node(2, Node(3, Node(4, common))))
ll2 = Node(6, Node(7, common))
find_intersecting_node(ll1, ll2)