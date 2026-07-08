
#|1 Right Rotate an Array by One Place without slicing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    n = len(x)
    for i in range(n-1,0,-1):
        x[i],x[i-1]=x[i-1],x[i]
rotate(nums)
print(nums)

#|= Right Rotate an Array by One Place with slycing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    n = len(x)
    nums[:] = x[n-1:]+x[:n-1]
rotate(nums)
print(nums)

#|1 Right Rotate an Array by k Place without slicing
nums = [5,-2,3,9,0,6,10,7]

def rotate(x, left, right):
    while left < right:
        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1

def right_rotate(nums, k):
    n = len(nums)
    if n == 0:          
        return
    k = k % n 

    rotate(nums, n-k, n-1)     
    rotate(nums, 0, n-k-1)     
    rotate(nums, 0, n-1)       

right_rotate(nums, 5)
print(nums)  

#-2 Right Rotate an Array by k Place without slicing
nums = []
def rotate(x):
    n = len(x)
    if n==0:
        return
    k = 11
    rotation = k%n
    for _ in range(0,rotation):         
        e = x.pop()
        x.insert(0,e)
rotate(nums)
print(nums)

#-3 Right Rotate an Array by k Place with slicing
nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    k = 13
    n = len(x)
    if n==0:
        return
    k = k%n
    x[:]=x[n-k:]+x[:n-k]
rotate(nums)
print(nums)

