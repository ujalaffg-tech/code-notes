
#| Implementing Linear Search
nums = [1,2,3,4,3]
def findd(x,target):
    
    for i in range(len(x)):
        if x[i]==target:
            return i
    return -1
print(findd(nums,4))