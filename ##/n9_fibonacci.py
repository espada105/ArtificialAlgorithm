def fibonacci(n):
    if n == 0:
        return 0 #기저사례
    elif n == 1:
        return 1 #기저사례
    else:
        return fibonacci(n-1) + fibonacci(n-2) #재귀호출
    
print(fibonacci(23))
