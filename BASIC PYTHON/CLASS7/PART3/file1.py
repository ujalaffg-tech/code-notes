
#: st se overwrite karane ke liye r+ ka use karenge
f = open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART3/file1.txt", "r+")
f.write("heynik05")
f.seek(0)
data = f.read()
print(data)
f.close()
## hamesha save karke run karo