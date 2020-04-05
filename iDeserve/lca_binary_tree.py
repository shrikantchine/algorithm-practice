"""
Find the lowest common ancestof of tht two given trees nodes
"""
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


def lca(root, A, B):
    # if Root is null return null
    if not root:
        return root

    # If root is either A or B return root
    if root == A or root == B:
        return root

    # Check the left subtree
    left = lca(root.left, A, B)

    # Check the right subtree
    right = lca(root.right, A, B)

    # if left and right are found, then return root
    if left and right:
        return root

    # if one of them is not null, return 
    if not left:
        return right
    if not right:
        return left


root = Node(9)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(5)

lca_node = lca(root, root.left, root.left.right.right)
print(lca_node)