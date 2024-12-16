class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None: #root가 없으면 Node(key)를 root로
        return Node(key)
    else:   # root가 있다면, 
        if root.val < key: #root의 val보다 key가 크면 right
            root.right = insert(root.right, key)
        else: #root의 val보다 key가 작으면 left
            root.left = insert(root.left, key)
        return root
    

r = Node(1)
r = insert(r, 2)

print(r.right)
# • 이진 트리 순회 방법
# • 전위 순회 (Pre-order): • 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리
# • 중위 순회 (In-order): • 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
# • 후위 순회 (Post-order): • 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트