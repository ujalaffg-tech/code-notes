
## hassing
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
hash_list = [0]*11
for val in n:
    hash_list[val] +=1
for i in m:
    if i<0 or i>10:
        print(0)
    else:
        print(hash_list[i])

s = "asdfsdsdssaaddasdwss"
y = ["a","s","d","f"]
hashlist =  [0]*26
for val in s:
    hashlist[ord(val)-ord('a')]+=1
for i in y:
    print(i,"-",hashlist[ord(i)-ord('a')])

s = "aA1bB2cC3dD4eE5fF6"
y = ["a", "b", "2", "A", "e", "3"]
lower_hash = [0] * 26
upper_hash = [0] * 26
digit_hash = [0] * 10
for val in s:
    if val.islower():
        lower_hash[ord(val)-ord('a')]+=1
    elif val.isupper():
        upper_hash[ord(val)-ord('A')]+=1
    elif val.isdigit():
        digit_hash[ord(val)-ord('0')]+=1
for ch in y:
    if ch.islower():
        print(ch,"-",lower_hash[ord(ch)-ord('a')])
    elif ch.isupper():
        print(ch,"-",upper_hash[ord(ch)-ord('A')])
    elif ch.isdigit():
        print(ch,"-",digit_hash[ord(ch)-ord('0')])

s = "asdfsdsdssaaddasdwss"
y = ["a","s","d","f"]
lower_hash = [0]*26
for val in s:
    if val.islower():
        lower_hash[ord(val)-ord('a')] +=1
for i in y:
    if i.islower():
        print(i,"-",lower_hash[ord(i)-ord('a')])