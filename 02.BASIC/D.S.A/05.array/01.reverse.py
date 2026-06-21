
#| Reverse an Array Using Recursion - 
nums = [4,5,6,545,7,2,3,0]
def reverses(x,left,right):
    if left>=right:
        return x
    x[left],x[right]=x[right],x[left]
    reverses(x,left+1,right-1)
reverses(nums,0,(len(nums)-1))
print(nums)
