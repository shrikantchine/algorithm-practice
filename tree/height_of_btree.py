class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    return max(height(root.left)+1,  height(root.right)+1)
    

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(4)
#root.right.right.right = Node(5)
print(height(root))