a = [[5,3],[1],[4,2,6]]
sorted_a = sorted(a,key=len)
print(sorted_a)

b = {'a':3, 'b':1,'c':2}
sorted_b = sorted(b.items(), key = lambda x: x[0])
print(sorted_b)
a = [[5,3],[1],[4,2,6]]
sorted_a = sorted(a,key=len)
print(sorted_a)

b = {'a':3, 'b':1,'c':2}
sorted_b = sorted(b.items(), key = lambda x: x[1])
print(sorted_b)

dict(sorted_b)