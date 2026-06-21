str1 = " this is a string .\n we are creating in python ."
print(str1)
print(len(str1))
str2 = " this is a string .\t we are creating in python ."
print(str2)

#:same line me print karane ke liye
print("hello" , end = " ")
print("aditya" , end = " " )
print("kumar" , end = "" )  ##same line but no space
print("nik")
#:alg line ke liye
print("hello" , end = "\n")
print("aditya" )

#: yah immutable hai
# name = "aditya"
# name[0]= "bicky"
# print(name)        error                       


#.indexing
str5 = "apna collage"
print(str5[4])       # a p n a    c o l l a 
print(str5[3])       # 0 1 2 3  4 5 6 7 8 9                                 
print(str5[0])

#.slicing
str6 = "apna collage"
print(str6[0:4])
print(str6[0:5])
print(str6[5:12])
# print(str6[5:len(str)])
#- print(str6[5:])
#- print(str6[:7])

#.negative index
str7 = "apple"     #  a  p   p l  e 
print(str7[-3:-1]) # -5 -4 -3 -2 -1

#.concatenation
first_name = "aditya"
second_name = "singh"
third = "5"
full_name = "abcd" + second_name + third
print(full_name)