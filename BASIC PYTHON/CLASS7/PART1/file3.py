f = open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART1/file3.txt")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5)
f.close()
## jitna bar readline() karoge utne time naya naya line print hoga
#: sara game corser ka hain
## ager next line exist karta hain to ak space line bhi print hoga 
## ager next line exist hi nahi karta to tab bhi space line 