class Node(object):
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next


def find_middle_elem(head):
    """
    We can use two pointer, slow and fast.
    fast pointer moves twice as fast as slow. 
    So, when the fast pointer reaches the end of linked list, slow pointer is at the middle element.
    """
    slow, fast = head, head
    while fast:      
        if fast.next == None or fast.next.next == None:
            fast = None
        else:
            slow = slow.next
            fast = fast.next.next
    return slow.val


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_middle_elem(head))

head2 = Node(1, Node(2, Node(3, Node(4))))
print(find_middle_elem(head2))

head3 = Node(1, Node(2))
print(find_middle_elem(head3))