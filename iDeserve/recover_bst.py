class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def recover_bst(root):
    travel = []
    inorder(root, travel)
    ooo = [] #Out of order
    find_out_of_order(travel, ooo)

    if len(ooo) == 0:
        print("Nothing is out of order")
    elif len(ooo) == 1:
        print(f"Nodes to swap - ({travel[ooo[0]-1]} - {travel[ooo[0]]})")
    elif len(ooo) == 2:
        print(f"Nodes to swap - ({travel[ooo[0]-1]} - {travel[ooo[1]]})")
    else:
        print("Something went wrong - {ooo}" )

def find_out_of_order(travel, ooo):
    for i in range(1, len(travel)-1):
        if travel[i-1] > travel[i]:
            ooo.append(i)

def inorder(root, travel):
    if not root:
        return
    inorder(root.left, travel)
    travel.append(root.data)
    inorder(root.right, travel)

root = Node(10)
root.left = Node(5)
root.left.left = Node(4)
root.left.right = Node(7)
root.right = Node(14)
root.right.left = Node(15)
root.right.right = Node(17)
recover_bst(root)