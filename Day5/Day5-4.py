class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.leftt = insert(root.left, key)
    return root

def pre_order(node):
    if node:
        print(node.vale)
        pre_order(node.self)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val, end='')

