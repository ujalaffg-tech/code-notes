
#| Remove Duplicates from a Sorted Array -
nums = []
def check(x):
        if len(x)<=0:
             return 0
        j = 1
        i = 0
        while j<len(x):
            if x[i] != x[j]:
                x[i+1],x[j]=x[j],x[i+1]
                i+=1
            j+=1
        return i+1
print(check(nums))

#- Remove Duplicates from a Sorted Array -
nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
    hashmap = {}
    for val in x:
        hashmap[val]=0
    j = 0
    for k in hashmap:
        x[j]=k
        j+=1
    return j
print(check(nums))


#- Remove Duplicates from a Sorted Array -
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