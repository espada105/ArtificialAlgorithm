def multi(y1, y2):
    resList = []
    res1 = y1 + y2
    res2 = y1 - y2
    resList.append(res1)
    resList.append(res2)
    return resList

mylist = []
hap, sub = 0,0

mylist = multi(100, 200)
hap = mylist[0]
sub = mylist[1]
print("multi에서 반환할 값 ==> %d %d" %(hap, sub))

    