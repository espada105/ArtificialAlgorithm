student1 = {'학번': 1000, '이름': "홍길동", '학과': "항공 컴퓨터 학과"}

student1['연락처'] = '010-1111-1111'

print(student1)

student1['학과'] = '파이썬학과'

print(student1)

print(student1['학번'])  
print(student1['이름'])  
print(student1['학과'])  

print(student1.get("이름"))

print(student1.get('주소', '주소가 없습니다'))  

print(student1.keys())

print(list(student1.keys()))

print(student1.values())

print(student1.items())
