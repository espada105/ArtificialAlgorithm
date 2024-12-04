class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
        else:
            new_node = Node(value)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node

