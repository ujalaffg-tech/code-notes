

#| bobble sort for assending order
nums = [5,8,1,6,9,2,4]
def func(x):
    l = len(nums)
    for j in range(l-1,0,-1):
        for i in range(j):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
func(nums)
print(nums)
#. T.C = 0(N**2)
#. S.C = 0(1) naya list nahi ban raha

#| bobble sort dessending order
nums = [5,8,1,6,9,2,4]
def func(x):
    l = len(nums)
    for j in range(l-1,0,-1):
        for i in range(j):
            if x[i]<x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
func(nums)
print(nums)
#. T.C = 0(N**2)
#. S.C = 0(1) 