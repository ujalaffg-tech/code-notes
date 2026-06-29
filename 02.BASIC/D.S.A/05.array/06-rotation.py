
#|= Right Rotate an Array by One Place with slycing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    nums[:] = [x[len(x)-1]]+x[0 : (len(x)-1)]
rotate(nums)
print(nums)

#= Right Rotate an Array by One Place without slicing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    n = len(x)
    for i in range(n-2,-1,-1):
        x[i+1],x[i]=x[i],x[i+1]
rotate(nums)
print(nums)

#|1 Right Rotate an Array by k Place without slicing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    n = len(x)
    k = 11
    rotation = k%n
    for _ in range(0,rotation):         
        e = x.pop()
        x.insert(0,e)
print(rotate(nums))
print(nums)

#|2 Right Rotate an Array by k Place with slicing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    k = 13
    n = len(x)
    k = k%n
    x[:]=x[n-k:]+x[:n-k]
print(rotate(nums))
print(nums)

#|3 Right Rotate an Array by k Place without slicing
nums = [5,-2,3,9,0,6,10,7]
k = 5
n = len(nums)
def rotate(x,left,right):
    while left<right:
        x[left],x[right]=x[right],x[left]
        left+=1
        right-=1
rotate(nums,(n-k),n-1)
rotate(nums,0,(n-k-1))
rotate(nums,0,n-1)
print(nums) 