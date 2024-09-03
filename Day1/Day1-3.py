def func1():
    global a
    a = 10
    print("func()1에서 a 값 %d" %a)

def func2():
    print("func()2에서 a 값 %d" %a)

a = 20

func1()
func2()