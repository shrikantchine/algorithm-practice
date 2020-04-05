class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def is_bst(root):
    return bst_util(root, [-1])

def bst_util(root, prev):
    if root.left:
        bst_util(root.left, prev)
    print(root.val, prev)
    if root.val < prev[0]:
        return False
    prev[0] = root.val
    if root.right:
        bst_util(root.right, prev)
    return True
    


root = Node(10, left=Node(7, right=Node(9)), right=Node(39))
print(is_bst(root))