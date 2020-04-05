class Node(object):
    def __init__(self, val, left=None, right=None, next_right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next_right = next_right


def connect(root):
    stack1 = [root]
    stack2 = []
    curr = None
    while len(stack1) > 0 or len(stack2) > 0:
        while len(stack1) > 0:
            if not curr:
                curr = stack1.pop()
            else:
                tmp = stack1.pop()
                curr.next_right = tmp
                curr = tmp
            if curr.left: stack2.append(curr.left)
            if curr.right: stack2.append(curr.right)
        curr = None
        while len(stack2) > 0:
            if not curr:
                curr = stack2.pop()
            else:
                tmp = stack2.pop()
                curr.next_right = tmp
                curr = tmp
            if curr.left: stack1.append(curr.left)
            if curr.right: stack1.append(curr.right)
            

