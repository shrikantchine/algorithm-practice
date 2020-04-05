class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def reverse(node):
    if not node:
        return node

    if not node.next:
        return node

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1


def print_ll(node):
    curr = node
    while curr.next:
        print(curr.data, end="  ")
        curr = curr.next
    print(curr.data)


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(head)
head = reverse(head)
print_ll(head)