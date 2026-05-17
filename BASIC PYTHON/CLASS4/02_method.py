info = {"class" : 10,
"sub" : ( "phy" , "chem" , "math" , "c++") ,
"digits":[1,2,34],
"food" : { "sun" : "nonveg",
"mon" : "nonveg" ,
"tue" : "veg"}}

#methods
#.keys()
print(info.keys())

#.values()
print(info.values())

#.items()
print(info.items())             #kay aur value dono ko tupple me

#.get("key")
print(info.get("class"))        # ye error dega hi nahi none print kara dega
print(info["class"])            # dict me class exist nahi karega to error dega
print(info["food"]["sun"])      #:nesting

#.update(" ":" ")
info.update({ "class" : 11,"city" : "patna"})
print(info)

#:second method
info["digits"] = [2,3,4]
print(info)
info["name"] = "aditya"
print(info)
info["food"] = { "sun" : "veg",
                 "mon" : "veg" ,
                 "tue" : "veg"}
print(info)
## ager key exist karega to update karega aur na ho to new add kar dega