class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        # 큐의 뒤에 항목 추가
        if len(self.queue) >= 5:
            self.queue.pop(0)
        self.queue.append(item)
        return self.queue[len(self.queue)-1]

    def dequeue(self):
        # 큐의 앞에서 항목 제거하고 반환 (FIFO)
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def sum(self):
        if not self.isEmpty():
            if len(self.queue) <= 5:
                return sum(self.queue)
            else:
                temp_queue = self.queue.copy()
                temp_queue.pop(0)
                return sum(temp_queue)
        return 0
    
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def get_last_n(self, n):
        if len(self.queue) < n:
            return self.queue
        return self.queue[-n:]

    def dequeue_multiple(self, n):
        items = []
        for _ in range(n):
            item = self.dequeue()
            if item is not None:
                items.append(item)
        return items

# 큐 인스턴스 생성
q = Queue()

# 항목 추가
for i in range(1, 8):
    q.enqueue(i)

# 뒤에서 5개 항목 가져오기
last_five = q.get_last_n(5)
# 앞에서 3개 항목 제거하기
first_three = q.dequeue_multiple(3)

# 앞에서 3개 항목의 합 구하기
sum_first_three = sum(first_three)

print(f"뒤에서 5개: {last_five} => 앞에서 3개: {first_three} => 합: {sum_first_three}")


