class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class CircularLinkedList:
    def __init__(self): #원형리스트의 초기화
        self.head =None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head: #리스트가 비어있을때
            self.head = new_node
            new_node.next = self.head #새 노드의 next를 자기로 설정(원형리스트 생성)
        else:
            temp = self.head 
            while temp.next != self.head: #마지막 노드 탐색, self.head부터 next가 self.head를 가르킬때까지
                temp = temp.next
            temp.next = new_node # 마지막 노드의 next를 새 노드로 설정
            new_node.next = self.head # 새 노드의 next를 head로 설정하여 원형 연결
    
    def delete(self, key):
        if self.head is None:
            return
        
        temp = self.head # 현재 노드를 head로 설정
        prev = None  # 이전 노드를 추적하기 위한 변수

        if temp.data == key: # 삭제하려는 key가 head의 데이터와 같은 경우
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return
    
    def search(self, key): # 현재 노드를 head로 설정
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
