
#| Remove Duplicates from a Sorted Array -
nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
        if len(x)==1:
             return 1
        j = 1
        i = 0
        while j<len(x):
            if x[i] != x[j]:
                x[i+1],x[j]=x[j],x[i+1]
            j+=1
        return i+1
print(check(nums))
print(nums)

#| Remove Duplicates from a Sorted Array -
nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
    dict = {}
    for val in x:
        dict[val]=0
    j = 0
    for k in dict:
        x[j]=k
        j+=1
    return j
print(check(nums))
print(nums)

#| Remove Duplicates from a Sorted Array -
nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
    i = 0
    j = 1
    while j<len(x):
        if x[i]==x[j]:
            x.remove(x[j])
        else:
            i+=1
            j+=1
check(nums)
print(nums)