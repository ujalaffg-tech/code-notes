
#.set 
#/ (unordered) means index ka kam nahi hai ✅
#/ (unique value) ✅
#/ float,int,bolean,str,tupple store hoga ✅
#/ dict,list store nahi hoga ✅
#: mutable
#~ iske ander ka elements immutable hain jaise str, int, tupple  

collection = {1,4,"stringcha", 4,(5,6,7)}
print(collection)
print(type(collection))

collection = set() #empty set
print(type(collection))

#methods
#.add(el)
collection = set()
collection.add(2)
collection.add("hey")
collection.add((3,4,5))##
print(collection)

#.remove(el)
collection.remove((2))
print(collection)

#.clear()
collection.clear()                      #empty set bana degaa
print(collection)
print(len(collection))

#.pop()
mynameis = {"aditya" , "laila" ,"nik"}  #random 1 element remove
mynameis.pop()
print(mynameis)

#: union and intersection
collection1 = {1,2,3,4,5}
collection2 = {3,4,5,6,7}
print(collection1.union(collection2))
print(collection1.intersection(collection2))