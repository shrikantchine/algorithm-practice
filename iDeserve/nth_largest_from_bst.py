class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def nth_largest(root, n, count=[0]):
    if not root:
        return
    nth_largest(root.right, n, count)
    count[0] += 1
    if count[0] == n:
        print(root.data)
        return
    nth_largest(root.left, n, count)


root = Node(10)
root.left = Node(7)
root.right = Node(12)
root.right.right = Node(13)
root.left.left = Node(5)
root.left.right = Node(9)
root.left.right.left = Node(8)
nth_largest(root, 4)