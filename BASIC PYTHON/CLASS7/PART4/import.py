
#. use of split
## string pe hi work karega
## split karega aur list me rakh dega
## default me space ke according todta hain 
data = "ka ho ka hal ba"
print(data.split())
 
x = "apple,banan,tree"
print(x.split(","))

student = ["aditya,75,88,99", "rahul,70,85,90"]
for val in student:
    print(val.split(","))

# .strip()
## ye bhi string pe hi kam karega
## string age piche ka space hata dega 
## bich ka space nahi hatayega
## new line \n ko bhi hata dega

x = " hello     " 
print(x.strip())
y = "\nAditya\n"
print(y.strip())
z = "    76"
print(z.strip())


'''import os 
os.remove("filepath")'''
