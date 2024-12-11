from collections import deque

class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value): #큐 "데이터" 추가
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    def peek(self): #큐의 left
        if self.is_empty():
            return None
        return self.queue.popleft
    
    def is_empty(self): #비어있는지
        return len(self.queue) == 0