class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        if abs(self.left.height() - self.right.height()) > 1:
            return False
        return True


    def height(self):
        if self.left is None and self.right is None:
            return 1
        return max(self.left.height(), self.right.height()) + 1


root = Node(5)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(6)
root.left.right = Node(10)
root.right.rigt = Node(11)

print(root.height())
print(root.is_balanced())