
#- PRINT NUMBERS FROM 1 TO 100
count = 1
while count <= 100:
    print(count)
    count += 1

#- PRINT NUMBERS FROM 100 TO 1
x = 100 
while x >= 1:
    print(x)
    x -= 1


#- PRINT THE ELEMENT OF THE  FOLOWING LIST USING A LOOP
[ 1,4,9,16,25,36,49,64,81,100]
nums = [ 1,4,9,16,25,36,49,64,81,100]
idx = 0 
while idx < len(nums):
    print(nums[idx])
    idx += 1

heroes = [ "ironman", "thor", "superman", "batman"]
idx = 0 
while idx<len(heroes):
    print(heroes[idx])
    idx += 1


#| SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
#[1,4,9,16,25,36,49,64,81,100]
t = (1,4,9,16,25,36,49,64,81,100)
find = 49
idx = 0 
while idx < len(t):
    if(t[idx]== find):
        print("finding index",idx)
    idx += 1 #idx+=1 ye if true hoga tab work karega
    #: ye while jab true hoga tabhi work karega
    
    
#- PRINT THE MULTIPLICATION TABLE OF A NUMBER N
number = int(input("table of : "))
n = int(input("nth time : "))
idx = 1
while idx <= n:
    print(number * idx)
    idx+=1  
