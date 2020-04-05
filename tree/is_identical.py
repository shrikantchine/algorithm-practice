class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1.val != root2.val:
        return False
    return (is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right))

root1 = Node(1, left=Node(2), right=Node(3))
root2 = Node(1, left=Node(3), right=Node(2))
print(is_identical(root1, root2))