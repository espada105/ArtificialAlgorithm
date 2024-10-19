class node:
    def __init__ (self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__ (self):
        self.head = None
    
    def append(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newnode
            newnode.next = self.head
    
    def remove(self,data):
        # 노드가 없을때
        if self.head is None:
            return
        temp = self.head
        prev = None

        # 삭제하려는게 첫 번째일때(마지막 노드를 두 번째노드로 연결)
        if temp.data == data:
            while temp.next != self.head:
                temp = temp.next
            # temp가 마지막노드면 통과

            temp.next = self.head.next #두 번째 노드로 연결
            self.head = self.head.next # 다시 self의 head를 지정
            return
        
        # 삭제하려는게 첫 번째 노드에 없을때 ()
        while temp.data != data: 
            prev = temp # prev에 self.head 지정
            temp = temp.next # temp에 self.head.next를 지정
            if temp.data == data:
                prev.next = temp.next
                return

# 결론은 지운다는 건 참조하는 것만 고치면됨