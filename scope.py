a="wow"

def f1():
    global a
    a="like"
    print(a)

def f2():
    a=50
    print(a)

f1()
f2()
print(a)
