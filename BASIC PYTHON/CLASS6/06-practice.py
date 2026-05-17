
#- print numbers from n to 1
def nums(x):
    if(x == 1): ## greter k bhi use kar sakte hain
        return 1 
    else:
        print(x)          ## ye print karayega
        return nums(x-1)  ## ye har bar uper jayega def me
print(nums(5))  

#- second method / socho socho
def sum(x):
    if(x == 0):
        return 
    else:
        print(x) 
        sum(x-1)
sum(5) 

#- factorial
def fact(x):
    if(x == 0):
        return 1
    return x * fact(x-1)
print(fact(5))
 
#- print numbers from 1 to n
def print_num(x , idx=1):
    if(idx == x+1):
        return
    else:
        print(idx)
        return print_num(x,idx+1)      ## ye har bar uper def me jayega
print_num(6)

#- sum of natural number
def calc_sum(x):
    if(x==0):
        return 0
    return x + calc_sum(x-1) 
print(calc_sum(5))

#| print sum of numbers from 1 to n
def natural_sum(x,idx=1):
    if idx == x+1 :
        return 0
    else:
        return idx + natural_sum(x,idx + 1)
print(natural_sum(5))

#- sum of natural number
def sum(x,idx=1,a=0):
    if(idx == x+1):
        return 
    else:
        a += idx
        print(a)
        return sum(x,idx+1,a)
sum(5)

#| list me present element ko line by line print karo
x = [1,3,5,7,9]
fruits = ["mango", "litchi", "apple", "banana"]
def print_list(list , idx= 0 ):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list ,idx+1)
print_list(x)
print_list(fruits)

#| sum of list in recursion
b = [1,3,5,7,9]
def linea(x,idx=0,a=0):
    if(idx == len(x)):
        print(a)
        return 0
    else:
        a += x[idx]
        return linea(x,idx+1,a)
linea(b)