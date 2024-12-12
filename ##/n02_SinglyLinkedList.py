class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)   #입력된걸 new_node로
        if self.head is None:   # head가 없다면
            self.head = new_node    #입력된 데이터를 head로
            print("Before return")
            return
        else:
            print('After return')   #head가 있다면
            last = self.head    #self.head를 last로
            while last.next:    #last.next가 없을때까지, 즉 last.next가 마지막일 때까지
                print('In while')
                last = last.next    #last.next 업데이트
            last.next = new_node    #while문에서 last.next가 비어있으니 여기에 new_node 넣으면 됨 ㅇㅇ..
    
    def delete(self, key):
        current = self.head #head를 current(현재노드)로
        if current and current.data == key: #current 존재, current.data==ket일때
            self.head = current.next #head(1개)만 있을때
            current = None # current를 없앰, 즉 현재노드를 비움
            return
        
        prev = None #prev
        while current and current.data != key: #current 존재, current.data가 key와 다르면 반복
            prev = current #이전 노드를 현재 노드로 업데이트
            current = current.next #현재노드를 다음 노드로 업데이트
        
        if current is None: #전부탐색했는데 key가 없다면
            return #종료
    
    def search(self, key):
        current = self.head
        while current: #current있으면 반복
            if current.data == key: 
                return True
            current = current.next
        return False #탐색다했는데 없으면 False 반환

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)

print(lst)


# 단순 연결 리스트의 시간 복잡도 
# 각 연산의 시간 복잡도
# 삽입: O(1) 끝에 삽입 시
# 삭제: O(n)
# 탐색: O(n)