from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()
        
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0