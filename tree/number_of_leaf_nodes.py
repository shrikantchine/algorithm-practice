class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leaf_node_count(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return leaf_node_count(root.left) + leaf_node_count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(4)
print(leaf_node_count(root))