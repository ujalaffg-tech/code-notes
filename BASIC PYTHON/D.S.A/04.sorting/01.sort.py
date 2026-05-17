
## sorting for assending order
nums = [5,7,8,4,1,6,9,2]
def func(x):
    for i in range(len(x)-1):
        miniidx = i
        for j in range(i+1,len(x)):
            if x[miniidx]>x[j]:
                miniidx = j
        x[i],x[miniidx] = x[miniidx],x[i]
    return x
print(func(nums))

## sorting for dessending order
nums2 = [5,7,8,4,1,6,9,2]
def func(x):
    for i in range(len(x)-1):
        maxidx = i
        for j in range(i+1,len(x)):
            if x[maxidx]<x[j]:
                maxidx = j
        x[i],x[maxidx]=x[maxidx],x[i]
    return x
print(func(nums2))