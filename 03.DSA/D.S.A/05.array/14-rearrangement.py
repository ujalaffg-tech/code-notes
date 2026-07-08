
#|1 Rearrange Array Elements by Sign - (optimal solution)
nums = [5,10,-3,-1,-10,6]
def check(x):
    n = len(x)
    result = [0]*n
    p = 0
    q = p+1
    for i in range(0,n):
        if x[i]>=0:
            result[p]=x[i]
            p+=2
        else:
            result[q]=x[i]
            q+=2
    return result
print(check(nums))

#- Rearrange Array Elements by Sign - 
nums = [5,10,-3,-1,-10,6]
def check(x):
    list1 = []
    list2 = []
    for val in x:
        if val>=0:
            list1.append(val)
        else:
            list2.append(val)
    i = 0
    n = len(list1)
    while i<n:
        x[i*2]=list1[i]
        x[(i*2)+1] = list2[i]
        i+=1
check(nums)
print(nums)
