
#| insertion sort for assending order
nums = [5,8,4,1,9,2,4]
def func(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i-1
        while j>=0 and key<x[j]:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
func(nums)
print(nums)
#. T.C = 0(n*n) i=2 to while loop 2 bar,3 par 3 bar
#. S.C = 0(1) naya list nahi ban raha


#| insertion sort for dessending order
nums = [5,8,4,1,9,2,4]
def func(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i-1
        while j>=0 and key>x[j]:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
func(nums)
print(nums)