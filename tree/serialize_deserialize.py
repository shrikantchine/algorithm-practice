class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    queue = [root]
    result = ''
    while queue:
        node = queue.pop(0)
        if node == 'N':
            result += ' N'
        else:
            result += ' ' + str(node.val)
            if not node.left and not node.right:
                continue
            queue.append(node.left if node.left else 'N')
            queue.append(node.right if node.right else 'N')
    return result
    
def deserialize(s, index=0):
    if index >= len(s):
        return None
    if s[index] == 'N':
        return None
    node = Node(int(s[index]))
    node.left = deserialize(s, index*2+1)
    node.right = deserialize(s, index*2+2)
    return node

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(3)
#root.right.right = Node(4)
print(serialize(root))

root = deserialize("1 2 2 3 4 3 N".split())
print("Shrikant")