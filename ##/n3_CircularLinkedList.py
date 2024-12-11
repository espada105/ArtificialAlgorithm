class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class CircularLinkedList:
    def __init__(self): #원형리스트의 초기화
        self.head =None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    
    def delete(self, key):
        if self.head is None:
            return
        
        temp = self.head
        prev = None

        if temp.data == key:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return
    
    def search(self, key):
        temp = self.head
        if temp is None:
            return False
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

# 원형리스트의 시간복잡도
# 삽입/삭제: O(n) 끝에 삽입 또는 삭제시 노드를 끝까지 찾아야됨
# 탐색:O(n) 리스트 전체를 돌아야됨
