# 리스트 컴프리헨션
# • 리스트 컴프리헨션은 리스트를 간결하게 만들 수 있는 방법임
# • 기존 리스트에서 조건을 걸거나 변형하여 새로운 리스트를 빠르게 생성할 수 있음

# 리스트 컴프리헨션
# • 형식
# • [expression for item in iterable if condition]
# • expression: 각 항목에 대해 실행할 표현식
# • item: 반복할 각 항목
# • iterable: 반복 가능한 객체 (리스트, 튜플 등)
# • condition: (선택적) 조건을 설정해서 항목을 필터링

a  = [x * 2 for x in range(10)]
print(a)

#조건 추가

b  = [x * 2 for x in range(10) if x % 2 == 0]
print(b)

# 중첩된 리스트 컴프리헨션
matrix = [[1,2,3],[4,5,6],[7,8,9]]
c = [[x ** 2 for x in row] for row in matrix]
print(c)
