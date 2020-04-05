class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_leaf_to_leaf_sum(root):
    update_tree(root)
    return root.val + (root.left.val if root.left else 0) + (root.right.val if root.right else 0)

def update_tree(root):
    if not root.left and not root.right:
        return
    if root.left:
        update_tree(root.left)
    if root.right:
        update_tree(root.right)  
    root.val += max(root.left.val if root.left else 0, root.right.val if root.right else 0)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(4)
print(max_leaf_to_leaf_sum(root))