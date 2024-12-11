# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


