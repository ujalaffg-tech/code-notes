nums = [5,8,1,6,9,2,4]
def func(x):
    for j in range((len(x)-2),-1,-1):
        for i in range(0,j+1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
func(nums)
print(nums)