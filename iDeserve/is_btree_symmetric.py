class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_symmetric(root):
    return symmetric_helper(root.left, root.right)

def symmetric_helper(n_left, n_right):
    if n_left is None and n_right is None:
        return True
    if (n_left is not None and n_right is None) or (n_right is not None and n_left is None):
        return False
    return (n_left.data == n_right.data) and symmetric_helper(n_left.left, n_right.right) and symmetric_helper(n_left.right, n_right.left)


root = Node(3)
root.left = Node(1)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(2)
root.right.left = Node(2)
root.right.right = Node(0)
root.left.left.left = Node(3)
root.left.right.right = Node(4)
root.right.left.left = Node(4)
root.right.right = Node(0)
root.right.right.right = Node(3)
print(is_symmetric(root))