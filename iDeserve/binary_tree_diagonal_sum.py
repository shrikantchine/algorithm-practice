class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

from collections import defaultdict

def diagonal_sum(root):
    dd = defaultdict(int)
    helper(root, 0, dd)
    print(dd)

def helper(root, curr_diagonal, dd):
    if not root:
        return
    helper(root.left, curr_diagonal+1, dd)
    dd[curr_diagonal] += root.data
    helper(root.right, curr_diagonal, dd)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left = Node(8)
root.right.right.left=Node(7)

diagonal_sum(root)