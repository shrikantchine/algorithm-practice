class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def btree_to_bst(root):
    in_order = []
    inorder(root, in_order)
    in_order.sort()
    reset_with_inorder(root, in_order)
    print("Shrikant") # Debug and check result :) 


def reset_with_inorder(root, in_order):
    if not root:
        return
    reset_with_inorder(root.left, in_order)
    x = in_order.pop(0)
    root.data = x
    reset_with_inorder(root.right, in_order)

def inorder(root, in_order):
    if not root:
        return
    inorder(root.left, in_order)
    in_order.append(root.data)
    inorder(root.right, in_order)


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.left.left.right = Node(6)
root.left.left.right.right = Node(8)
root.right.left.right=Node(7)
btree_to_bst(root)