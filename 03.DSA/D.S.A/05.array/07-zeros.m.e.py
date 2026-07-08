
#|1 Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def check(x):
    
    n = len(x)
    for i in range(0,n):
        if x[i]==0:
            break
    else:
        return
    
    j = i+1
    while j<n:
        if x[j]!=0:
            x[i],x[j]=x[j],x[i]
            i+=1
        j+=1
    
check(nums)
print(nums)

#|- Move Zeros to the End of the List -
nums = [1,2,0,4,3,0,0,3,5,1]
def check(x):

    n = len(x)
    result = []
    for val in x:
        if val != 0:
            result.append(val)
    i = 0
    for val2 in result:
        x[i]=val2
        i+=1

    for  j in range(i,n):
        x[j]=0
    return result

check(nums)
print(nums)

