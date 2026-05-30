
#| insertion sort for assending order
nums = [5,8,1,6,9,2,4]
def func(x):
    l = len(x)
    for i in range(1,l):
        key = nums[i]
        j = i-1
        while j>=0 and x[j]>key:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
func(nums)
print(nums)

#| insertion sort for assending order
nums = [5,8,1,6,9,2,4]
def func(x):
    l = len(x)
    for i in range(1,l):
        key = x[i]
        j = i-1
        while j>=0 and x[j]<key:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
func(nums)
print(nums)