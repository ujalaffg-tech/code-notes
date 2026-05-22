
#|1
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
hash_list = [0]*11
for val in n:
    hash_list[val] +=1
for i in m:
    if i>=0 and i<=10:
        print(i,"-",hash_list[i])
    else:
        print(i,"-",0)
#. T.C = 0(M+N)
#. S.C = 0(1)

#|2
s = "asdfsdsdssaaddasdwss"
y = ["a","s","d","f"]
hash_list = [0]*26
for val in s:
    hash_list[ord(val)-ord('a')]+=1
for i in y:
    print(i,'-',hash_list[ord(i)-ord('a')])
#. T.C = 0(S+Y)
#. S.C = 0(1)

#|3
s = "aA12baaB22cC3A222A3dD43eE5QAf2F6"
y = ["a", "b", "2", "A", "e", "3"]
hash_lower = [0]*26
hash_upper = [0]*26
hash_digit = [0]*10
for val in s:
    if val.islower():
        hash_lower[ord(val)-ord('a')]+=1
    elif val.isupper():
        hash_upper[ord(val)-ord('A')]+=1
    elif val.isdigit():
        hash_digit[ord(val)-ord('0')]+=1
for i in y:
    if i.islower():
        print(i,"-",hash_lower[ord(i)-ord('a')])
    elif i.isupper():
        print(i,"-",hash_upper[ord(i)-ord('A')])
    elif i.isdigit():
        print(i,"-",hash_digit[ord(i)-ord('0')])
#. T.C = 0(S+Y)
#. S.C = 0(1)
