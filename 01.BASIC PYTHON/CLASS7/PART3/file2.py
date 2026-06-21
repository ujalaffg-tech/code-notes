
#: file ka data clear karke naya data likhne ke liye w+
f = open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART3/file2.txt", "w+")
f.write("abc")
f.seek(0)
print(f.read())
f.close()