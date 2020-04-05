class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def min_height(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return min(min_height(root.left), min_height(root.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)
root.left.left.right.left = Node(11)
root.left.right.right = Node(9)
root.right.right.right = Node(10)

print(min_height(root))