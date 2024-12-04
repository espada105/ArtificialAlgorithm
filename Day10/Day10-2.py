class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0

    def reverse_string(self, input_string):
        for char in input_string:
            self.push(char)
        reversed_string = ''
        while not self.is_empty():
            reversed_string += str(self.pop())  
        return reversed_string

Stack = stack()


Stack.push("1")
Stack.push("2")
Stack.push("3")

print(Stack)


reversed_str = Stack.reverse_string("안녕하세요")
print(reversed_str)  