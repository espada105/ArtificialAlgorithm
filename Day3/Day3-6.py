katok =['다현','정연','쯔위','사나','지효']

def del_data(position):
    if position < 0 or position >len(katok):
        print("데이터를 삭제할 범위를 벗어남")
        return
    
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[[kLen-1]])

del_data(1)
print(katok)
del_data(3)
print(katok)