class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_mirror(root):
    return mirror_util(root.left, root.right)

def mirror_util(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1.val != root2.val:
        return False
    return mirror_util(root1.left, root2.right) and mirror_util(root1.right, root2.left)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(4)
print(is_mirror(root))