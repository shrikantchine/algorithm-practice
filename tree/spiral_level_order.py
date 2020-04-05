class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def spiral_level_order(root):
    stack1 = [root]
    stack2 = []
    while len(stack1) > 0 or len(stack2) > 0:
        while len(stack1) > 0:
            curr = stack1.pop()
            print(curr.val, end="  ")
            if curr.right: stack2.append(curr.right)
            if curr.left: stack2.append(curr.left)
                      
        while len(stack2) > 0:
            curr = stack2.pop()
            print(curr.val, end="  ")
            if curr.left: stack1.append(curr.left)
            if curr.right:stack1.append(curr.right)
            
                
        
root = Node(20)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
root.right.left = Node(50)

spiral_level_order(root)