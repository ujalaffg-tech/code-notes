
#: last me kuch add karwana ho to a+ ka use karenge
f = open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART3/file3.txt","a+")
f.write(" heynik05")
f.seek(0)
print(f.read())
f.close()