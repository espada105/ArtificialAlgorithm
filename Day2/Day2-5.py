ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 재밌지는 않고 ^^'

print(ss.count('공부'))  

print(ss.find('공부'), ss.find('공부', ss.find('공부') + 1), ss.find('없다'))

print(ss.index('공부'), ss.index('공부', ss.index('공부') + 1))

print(ss.startswith('파이썬'), ss.endswith('^^'))
