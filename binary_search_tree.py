class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        ret = ""
        if level > 0:
            ret += (level-1)*"  "+"|__"
        ret += "  "*level+str(self.val)+"\n"
        if self.left:
            ret += self.left.__str__(level=level+1)
        if self.right:
            ret += self.right.__str__(level=level+1)
        return ret

class BST(object):
    def __init__(self, root=None):
        self.root = root

    def add_several(self, arr):
        for x in arr:
            self.add(x)

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.__add_helper(val, self.root)

    def __add_helper(self, val, n):
        if n.val > val:
            if n.left is None:
                n.left = Node(val)
            else:
                self.__add_helper(val, n.left)
        else:
            if n.right is None:
                n.right = Node(val)
            else:
                self.__add_helper(val, n.right)

    
    def height(self, n=None):
        if n is None:
            n = self.root
        if n.left is None and n.right is None:
            return 1
        lh, rh = 0, 0
        if n.left is not None:
            lh = self.height(n.left)
        if n.right is not None:
            rh = self.height(n.right)
        return max(lh, rh) + 1

    def inorder(self):
        if self.root is None:
            return None
        return self.__inorder_helper(self.root)
    
    def __inorder_helper(self, n):
        result = []
        if n.left is not None:
            result.extend(self.__inorder_helper(n.left))
        result.append(n.val)
        if n.right is not None:
            result.extend(self.__inorder_helper(n.right))
        return result

    def balance(self):
        inorder = self.inorder()
        self.root = self.__balance_helper(inorder)

    def __balance_helper(self, inorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return Node(inorder[0])
        mid = len(inorder)//2
        node = Node(inorder[mid])
        node.left = self.__balance_helper(inorder[:mid])
        node.right = self.__balance_helper(inorder[mid+1:])
        return node

    def preorder(self):
        if self.root is None:
            return None
        return self.__preorder_helper(self.root)

    def __preorder_helper(self, node) :
        result = []
        result.append(node.val)
        if node.left:
            result.extend(self.__preorder_helper(node.left))
        if node.right:
            result.extend(self.__preorder_helper(node.right))
        return result

    def postorder(self):
        if self.root is None:
            return None
        return self.__postorder_helper(self.root)

    def __postorder_helper(self, node) :
        result = []
        if node.left:
            result.extend(self.__postorder_helper(node.left))
        if node.right:
            result.extend(self.__postorder_helper(node.right))
        result.append(node.val)
        return result

    def level_order(self):
        result = []
        stack = [self.root]
        while len(stack) != 0:
            node = stack[0]
            stack = stack[1:]
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.append(node.val)
        return result



    def __str__(self):
        return str(self.root)


bst = BST()
bst.add_several([2, 3, 5, 7, 1, 9,0])
print(bst.height())
print(bst.inorder())
print(bst.balance())
print(bst.inorder())
print(bst.height())
print(bst.preorder())
print(str(bst))
print(bst.postorder())
print(bst.level_order())