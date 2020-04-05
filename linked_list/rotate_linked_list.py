class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rotate(head, by=1):
    end = head
    while end.next:
        end = end.next
    while by >0 :
        tmp = head
        head = head.next
        tmp.next = None
        end.next = tmp
        end = end.next
        by -= 1
    return head

def print_ll(head):
    curr = head
    while curr.next:
        print(f"{curr.val} -> ", end='')
        curr = curr.next
    print(curr.val)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(head)
new_head = rotate(head, 3)
print_ll(new_head)