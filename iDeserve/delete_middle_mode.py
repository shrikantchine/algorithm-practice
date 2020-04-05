class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def delete_middle_node(head):
    slow = None
    fast = head
    prev = None
    while fast:
        prev = slow
        slow = slow.next if slow else head
        fast = fast.next
        if fast:
            fast = fast.next

    prev.next = slow.next

    curr = head
    while curr.next:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(curr.data)


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
delete_middle_node(head)