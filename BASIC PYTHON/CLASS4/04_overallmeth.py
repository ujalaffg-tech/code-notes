
#: immumutable hai to direct print()
##  mutable me dekhna hai value change kar raha hain ya nahi
## mutable no change direct print()
## mutable value change kare tab, methods likh ke print() karo
#.str(immutable)
str1 = " I am studing python from Apnacollege"
print(str1.replace("python","Java"))

#.list(mutable)
digit = [2,5,8,6,1,9]
digit.sort()
print(digit)

#.tupple(immutable)
digit = (2,5,2,8,6,1,9)
print(digit.index(2))

#.dict(mutable)
school_info = {"class" : 10,
"sub" : ( "phy" , "chem" , "math" , "c++") ,
"food" : { "sun" : "nonveg",
"mon" : "nonveg" ,
"tue" : "veg"}}
print(school_info.values())
school_info.update({"class" : 11})
print(school_info)

#.set(mutable)
collection = {2,4,4,"hey", "nik"}
collection.add(500)
print(collection)