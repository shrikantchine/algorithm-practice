class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def left_view(node, result=[]):
    if not node:
        return []
    queue = []
    level = 0
    level_added = 0
    result = []
    queue.append((node, level))
    while len(queue) > 0:
        n = queue.pop(0)
        if n[1] == level_added and n[0].val != 'N':
            result.append(n[0].val)
            level_added += 1
        level += 1
        if n[0].left:
            queue.append((n[0].left, level))
        if n[0].right:
            queue.append((n[0].right, level))
     
    return result


def left_view_rec(root, level=0, max_level=0):
    if not root:
        return
    if max_level < level:
        print(f"{root.val}  ", end='')
        max_level = level
    left_view_rec(root.left, level+1, max_level)
    left_view_rec(root.right, level+1, max_level)



root = Node(10, left=Node(20, left=Node(40), right=Node(60)), right=Node(30))
print(left_view(root))
left_view_rec(root)