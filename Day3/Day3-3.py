katok =['다현','정연','쯔위','사나','지효']
katok.append(None)
for i in range(len(katok) -1, 0 , -1):
    katok[i] = katok[i-1]
    katok[i-1] = None
katok[0]='모모'
print(katok)


