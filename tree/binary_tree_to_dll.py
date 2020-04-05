class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

head = None
prev = None

def binary_tree_to_dll(root):
    inorder(root)
    curr = head
    while curr:
        print(curr.val, end='  ')
        curr = curr.right
    curr = prev
    print()
    while curr:
        print(curr.val, end='  ')
        curr = curr.left
    

def inorder(root):
    global head
    global prev
    if not root:
        return
    inorder(root.left)
    if not prev:
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    inorder(root.right)

root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(60)
root.right = Node(30)
binary_tree_to_dll(root)