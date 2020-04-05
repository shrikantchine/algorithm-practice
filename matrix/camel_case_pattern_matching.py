class Node(object):
    def __init__(self, val, is_leaf=False):
        self.val = val
        self.is_leaf = is_leaf
        self.children = []

    def get_child(self, pattern):
        if len(self.children) == 0:
            return None
        for child in self.children:
            if child.val == pattern:
                return child
        return None

    def get_leaves(self):
        if self.is_leaf:
            return self.val
        result = []
        for child in self.children:
            result.extend(child.get_leaves())
        return result

def camel_case_matching(dictionary, pattern):
    root = preprocess(dictionary)
    search_result = search(root, pattern)
    return ''.join(search_result)

def search(node, pattern):
    if len(pattern) == 0:
        return node.get_leaves()
    child = node.get_child(pattern[0])
    if not child:
        print("Pattern not found")
        return []
    return search(child, pattern[1:])

def preprocess(dictionary):
    root = Node('')
    for i in dictionary:
        add_word_to_trie(root, i, [x for x in i if x.isupper()])
    return root

def add_word_to_trie(node, word, camel_case_letters):
    if len(camel_case_letters) == 0:
        node.children.append(Node(word, is_leaf=True))
        return
    child = node.get_child(camel_case_letters[0])
    if not child:
        child = Node(camel_case_letters[0])
        node.children += [child]
    add_word_to_trie(child, word, camel_case_letters[1:])
    
    
result = camel_case_matching(['WelcomeGeek', 'WelcomeToGeeksForGeeks', 'GeeksForGeeks'], 'WTG')
print(result)