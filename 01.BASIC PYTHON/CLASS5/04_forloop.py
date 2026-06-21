# print the elements of the  list using a Loop 
nums = [ 1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

#| Search for a number x in this tuple using loop:
nums = [1,4,9,16,25,36,49,9,64,81,100,49, 49]

x = 49
idx = 0
for val in nums:
    if(val == x):
        print("number found at index",idx)
        idx += 1
    