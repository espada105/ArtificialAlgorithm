class node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next: 
                current = current.next #다음노드로 변경하는 거임 
                # current.next가 none이 아니면 다음노드를 찾는다
                # 다시말해 head가 1이면 1의 다음인 2가 current가 된다 
                # 그리고 2다음이 NONE이면 NEWNODE가 none 의 자리에 들어간다
            current.next = newnode