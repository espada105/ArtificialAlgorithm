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
    
    def sum_of_last_five(self,numbers):
        queue = deque()
        current_sum = 0

        for num in numbers:
            queue.append(num)
            current_sum +=num

            if len(queue) > 5:
                oldest_num = queue.popleft()
                current_sum -= oldest_num
            
            print(f"입력:{num} -> 출력: {current_sum}")

numbers = [1,2,3,4,5,6,7]

s1 = queue()
s1.sum_of_last_five(numbers)


# 입력:1 -> 출력: 1
# 입력:2 -> 출력: 3
# 입력:3 -> 출력: 6
# 입력:4 -> 출력: 10
# 입력:5 -> 출력: 15
# 입력:6 -> 출력: 20
# 입력:7 -> 출력: 25

# 1-5까지 들어왔을때 15이고 
# 6이 추가로 들어오면서 if문에서 5개보다 값이 많으면 자름
# 그래서 가장 FIFO에 따라 1이 먼저사라짐
# 1얘가 떨어져나감  2,3,4,5  +  6