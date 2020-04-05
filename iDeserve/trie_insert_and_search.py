class Node(object):
    def __init__(self, data, children=[]):
        self.data = data
        self.children = []

    def get_child(self, data):
        for x in self.children:
            if x.data == data:
                return x
        return None

class Trie(object):
    def __init__(self):
        self.root = Node('')

    def insert(self, data):
        self.insert_helper(self.root, data, 1)
        print(f"{data} added")

    def insert_helper(self, node, data, index):
        if index > len(data):
            return
        child = node.get_child(data[:index])
        if not child:
            child = Node(data[:index])
            node.children.append(child)
        self.insert_helper(child, data, index+1)

tt = Trie()
tt.insert('cat')