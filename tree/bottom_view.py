class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bottom_view(root):
    level_dict = {}
    level_order(root, level_dict)
    print(level_dict)
    for key in sorted(level_dict.keys()):
        print(f"{level_dict[key]}  ", end='')

def level_order(root, level_dict):
    stack = [(root, 0)]
    while len(stack) > 0:
        curr = stack.pop(0)
        level_dict[curr[1]] = curr[0].val
        if curr[0].left:
            stack.append((curr[0].left, curr[1]-1))
        if curr[0].right:
            stack.append((curr[0].right, curr[1]+1))


root = Node(20)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
root.right.left = Node(50)

bottom_view(root)