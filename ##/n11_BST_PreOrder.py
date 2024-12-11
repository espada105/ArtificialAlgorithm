class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preOrder(node):
    if node:
        print(node.val)
        preOrder(node.left)
        preOrder(node.right)

def insert(root, key):
    if root is None: 
        return Node(key) 
    else:
        if root.val < key: #root보다 key가 크면 
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

r = Node(10)
r = insert(r, 20)
r = insert(r, 7)
r = insert(r, 3)
r = insert(r, 15)
preOrder(r)