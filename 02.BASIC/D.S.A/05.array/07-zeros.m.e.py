
#|1 Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def chek(x):
    temp = []
    m = len(x)
    for val in x:
        if val!=0:
            temp.append(val)
    n = len(temp)
    for i in range(0,n):
        x[i]=temp[i]
    for j in range(n,m):
        x[j]=0
chek(nums)
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

