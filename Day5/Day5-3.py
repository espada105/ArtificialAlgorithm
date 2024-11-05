class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def inser(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = inser(root,right, key)
        else:
            root.leftt = inser(root,left, key)
    return root

