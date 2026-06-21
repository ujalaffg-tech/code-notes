
#| Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def zeros(x):
    temp = []
    for val in x:
        if val>0:
            temp.append(val)
    
    for i in range(0,len(temp)):
            x[i]= temp[i]
    for j in range(len(temp),len(x)):
        x[j]=0
    
zeros(nums)
print(nums)

#|2 Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def zeroo(x):
    if len(x)==1:
        return
    i = 0
    while i < len(x):
        if x[i]==0:
            break
        i+=1
    if i==len(x):
        return
    j = i+1
    while j<len(x):
        if x[j]!=0:
            x[i],x[j]=x[j],x[i]
            i+=1
        j+=1
zeroo(nums)
print(nums)

## Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def zeros(x):
    i = 0
    j = 1
    n = len(x)
    if n==1:
        return
    while j<n and n>1 :
        if x[i]==0 and x[j]==0:
            j+=1
        elif x[i]==0 and x[j]!=0:
            x[i],x[j]=x[j],x[i]
            i+=1
            j+=1
        else:
            i+=1
            j+=1
zeros(nums)
print(nums)
