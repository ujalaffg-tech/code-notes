
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for val in n:
    dict[val] = dict.get(val,0)+1
for i in m:
    if i in dict:
        print(i,"-",dict[i])
    else:
        print(i,"-",0)
