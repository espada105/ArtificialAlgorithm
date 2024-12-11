from collections import deque

def sum_of_last_five(numbers):
    queue = deque()
    current_sum = 0

    for num in numbers:
        queue.append(num)
        current_sum += num

        if len(queue) > 5:
            oldest_num = queue.popleft()
            current_sum -= oldest_num

        print(f"입력:{num} => 출력: {current_sum}")

numbers = [1,2,3,4,5,6,7]
sum_of_last_five(numbers)