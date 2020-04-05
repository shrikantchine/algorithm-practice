class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, n1, n2):
    # if n1 belongs in subtree of n2 return n2
    # if n2 belongs if subtree of n1 return n1
    if root.val == n1 or root.val == n2:
        return root.val

    # if n1 belongs in left subtree of root and n2 belongs in right subtree of root, return root
    if n1 <= root.val and n2 > root:
        return root.val

    # if n2 belongs in left subtree of root and n1 belongs in right subtree of root return root
    if n2 <= root.val and n1 > root:
        return root.val

    # Otherwise recurse on the tree n1 and n2 belong to
    if n1 <= root.val and n2 <= root.val:
        return lowest_common_ancestor(root.left, n1, n2)
    if n1 > root.val and n2 > root.val:
        return lowest_common_ancestor(root.right, n1, n2)

root = Node(5)
root.left = Node(4)
root.left.left = Node(3)
root.right = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

print(lowest_common_ancestor(root, 7, 8))