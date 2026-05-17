
#- tail recursion
count = 0
def func():
    global count
    if count==3:
        return
    count+=1
    func()
    print("aditya")
func()

#- head recursion
def func(x,n):
    if(n==0):
        return
    print(x)
    func(x,n-1)
func(15,4)

#- print 1 to n using head recursion
def func(x,n):
    if x>n:
        return
    print(x)
    func(x+1,n)
func(1,15)

#- print 1 to n using tail recursion
def func(n):
    if n==0:
        return
    func(n-1)
    print(n)
func(4)

#- parametrized recursion
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,5)

#| functional recursion
def func(n):
    if n==1:
        return 1
    return n + func(n-1)
func(5)

#- find factorial
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))