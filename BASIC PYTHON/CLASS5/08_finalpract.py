
#- WAP to find the sum of first n natural numbers. (using while)
n = int(input("enter number :"))
idx = 1
val = 0
while idx <= n:
    val += idx
    idx+=1
print(val)

#- WAP to find the sum of first n natural numbers. (using for)
n = int(input("enter number : "))
idx = 0
for val in range(1, n+1):
    idx+=val
print(idx)

#| WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS .(USING FOR)
n = 5
idx = 1
for val in range(1,n+1):
    idx = idx*val
    #print(idx) yaha print likha to yeh bhi loop me ake kam karne lagega
print(idx)

#| WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS .(USING while)
n = 5
idx = 1
a = 1
while idx<=n: 
    a = idx *a
    idx+=1
print(a)
 


    
    
