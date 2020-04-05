class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_bst(arr):
    n = len(arr)
    if n == 0:
        return None
    mid = n//2
    root = Node(data=arr[mid])
    root.left = build_bst(arr[0:mid])
    root.right = build_bst(arr[mid+1:])
    return root




root = build_bst([1, 2, 3, 4, 5, 6])
# Tested in debug