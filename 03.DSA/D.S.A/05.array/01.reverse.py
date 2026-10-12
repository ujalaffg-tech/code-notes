
#| Given an integer array nums, reverse the array in-place 
#| You are not allowed to use any extra array or built-in reverse 
#| methods.Modify the original array and return nothing. 

nums = [4,5,6,545,7,2,3,0]
def reverses(x,left,right):
    while left<right: 
        x[left],x[right]=x[right],x[left]
        left+=1
        right-=1
reverses(nums,0,(len(nums)-1))
print(nums)


#. T.C = O(N/2) 0R 0(N)
#. S.C = O(1)