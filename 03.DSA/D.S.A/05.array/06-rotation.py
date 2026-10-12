
#|1 Given an integer array nums, rotate the array to the right 
#|  by one position. Modify the array in-place without using slicing
#|  or any extra array.

nums = [5,-2,3,9,0,6,10,7]
def rotate(x):
    n = len(x)-1
    for i in range(n,0,-1):
        x[i],x[i-1]=x[i-1],x[i]
rotate(nums)
print(nums)

#. T.C = O(N)
#. S.C = O(1)

#|= Given an integer array nums, rotate the array to the right 
#|= by one position using Python slicing.

nums = [5,-2,3,9,0,6,10,7]
def check(x):
    n = len(x)-1
    x[:]=x[n:]+x[:n]
check(nums)
print(nums)

#. T.C = O(N)
#. S.C = O(N)

#| Given an integer array nums and an integer k, rotate the 
#|  array to the right by k positions. You must solve the problem
#|  in-place, without using slicing or an extra array. If k is greater 
#|  than the length of the array, rotate by k % n positions.

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

#-2 Given an integer array nums and an integer k, rotate the 
#-  array to the right by k positions by repeatedly performing one 
#-  right rotation at a time. If k is greater than the length of the array, 
#-  rotate by k % n positions.

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

#. T.C = O(K * N) where k is number of rotation
#. S.C = O(1)

#-3 Given an integer array nums and an integer k, rotate the 
#-  array to the right by k positions using Python slicing. If k is 
#-  greater than the length of the array, rotate by k % n positions.

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

#. T.C = O(N)
#. S.C = O(N)
