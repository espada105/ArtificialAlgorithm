class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.val, end="") #root
