
#: break and continue whileloop or forloop dono me kam karta hain 
count = 1
while count <=10:
    print(count)
    if(count == 5):
        break
    count+= 1

##
nums = (1,4,9, 16,100,25,36,49,64,81,100,36)
found = 100
idx = 0
while idx<len(nums):
    if(nums[idx] == found):
        print(idx)
        break       #break likhne se idx 4 pe ruk gya 
    else:
        print("finding") # if ke samne use karo

    idx += 1
           
#= 1 se 10 ke bich odd number print karo
st = 1 
while st <=10:
    if(st%2 != 0):
        st += 1 ### logic
        continue
    print(st)
    st += 1    