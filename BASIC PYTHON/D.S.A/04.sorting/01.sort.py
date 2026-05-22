
#| sorting for assending order
nums = [5,7,8,4,1,6,9,2]
def func(x):
    l = len(x)
    for i in range(l-1):
        miniidx = i
        for j in range(i+1,l):
            if x[miniidx]>x[j]:
                miniidx = j
        x[i], x[miniidx] = x[miniidx], x[i]
func(nums)
print(nums)
#. T.C = 0(N**2)
#. S.C = 0(1) naya list nahi ban raha


#| sorting for dessending order
nums = [5,7,8,4,1,6,9,2]
def func(x):
    l = len(x)
    for i in range(l-1):
        maxidx = i
        for j in range(i+1,l):
            if x[maxidx] < x[j]:
                maxidx = j
        x[i], x[maxidx] = x[maxidx], x[i]
func(nums)
print(nums)
