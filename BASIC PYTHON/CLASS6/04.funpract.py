
#- square return kare
def print_sq(x):
    result = x*x
    print(result)
print_sq(5)

#- sum of 2 numbers
def print_sum(a,b):
    sum = a+b
    print(sum)
print_sum(2,4)

#- check number is odd or even
def check(nums):
    if(nums%2== 0 ):
        print("even")
    else:
        print("odd")
check(5)

#- len of str
def str_len(str):
    print(len(str))
str_len("thikba")

#| WAF to convert USD to INR.
def in_inr(usd):
    inr = usd * 83
    print(usd ,"$ =" , inr , "₹")

in_inr(50)

#| greatest no in 3 elements
def grt_nums(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b) 
    else:
        print(c) 
grt_nums(4,900,98)

#| return ke bad value likhoge tab none nahi ayega
#= greatest elements
def grt_nums(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b 
    else:
        return c
result = grt_nums(4,900,98)
print(result)

#| factorial
def print_fact(x):
    idx = 1
    val = 1
    while idx <= x:
        val*=idx
        idx+=1
    print(val)
print_fact(7)

#| factorial
n = 5 
def fact(x):
    idx =1
    for val in range(1,x+1):
        idx*=val
    print(idx)
fact(n)

#| sum of list 
list = [1,2,3,4,6,7,4]
def sum_of_list(x):
    idx = 0
    sum = 0
    while idx <len(x):
        sum+=x[idx]
        idx+=1 ## iska indentation piche kyu nahi kyuki loop bana rahe 
    print(sum) ## loop khatam
sum_of_list(list)
  
#| sum of list 
list = [1,2,3,4,6,7,4]
def sum_of_list(x):
    sum = 0 
    for item in x:
        sum+=item
    print(sum)
sum_of_list(list)