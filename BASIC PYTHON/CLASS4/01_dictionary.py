info = {"name" : "aditya",
#: name ko yaha key bolenge aur aditya ko value 
"age"  : 19,
12.99 : 94.55}
print(info)         ## aur dictionary me jyada tar key str lete ,
print(type(info))   ## kabhi int,float ,vagaira ka bhi use kr lete hai 
print(info["name"]) 
print(info[12.99]) 
print(len(info))

#: empty dict
a = {}
print(type(a))

x = {}
x["eng"] = "chutiya"
x[5] = 5.0
print(x)

#: ye mutable hai
d = { "name":"adi"}
d["name"] = "aditya" ##
print(d)

#: naya key add karne ke liye
d = { "name":"adi"}
d["surname"] = "aditya"
print(d)

## get key in full details 
dict = {"name" : "aditya"}
print(dict.get("name"))
print(dict.get("name","unknown")) ## already key exist
print(dict.get("age",0))
print(dict)

#| overall
print(dict.get("age",0)) ## - 0
print(dict.get("x",5)) ##  -5
## dict.get val deta hain key ka 

d = [2,3,4,5,3,4,2,34,4,3]
dict = {}
for val in d:
    dict[val] = dict.get(val,0)+1
print(dict)
