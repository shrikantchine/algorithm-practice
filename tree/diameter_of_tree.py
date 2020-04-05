class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def height(root):
    if root is None:
        return 0
    return max(height(root.left)+1,  height(root.right)+1)