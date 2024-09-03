def func1():
    a = 10
    print("func1()에서 a 값 %d" %a)
    
def func2():
    print("func1()에서 a 값 %d" %a)

a = 20

func1()
func2()