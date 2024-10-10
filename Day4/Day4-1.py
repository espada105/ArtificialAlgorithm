class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print('before return')
            return
        
        print('after return')
        last = self.head
        while last.next:
            print('In while')
            last = last.next
        last.next = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print('The given previous node must be in LinkedList')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.value == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.value == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.value == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

i_list = LinkedList()
print("--------------")
i_list.append(1)
print("--------------")
i_list.append(2)
print("--------------")
i_list.append(3)
print("--------------")
