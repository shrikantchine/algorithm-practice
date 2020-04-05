from collections import defaultdict

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_traverse(root):
    level_dict = defaultdict(list)
    queue = [(root, 0)]
    while len(queue) > 0:
        curr = queue.pop(0)
        level_dict[curr[1]].append(curr[0].val)
        if curr[0].left:
            queue.append((curr[0].left, curr[1]-1))
        if curr[0].right:
            queue.append((curr[0].right, curr[1]+1))
    
    print(level_dict)
    result = []
    for key in sorted(level_dict.keys()):
        result.extend(level_dict[key])
    print(result)



root = Node(20)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
root.right.left = Node(50)

vertical_traverse(root)