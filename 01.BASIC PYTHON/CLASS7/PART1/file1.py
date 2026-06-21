f = open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART1/file1.txt", "r")
f.seek(0)
data = f.read()
print(data)
print(type(data))
f.close()

## DEFAULT- "R"
