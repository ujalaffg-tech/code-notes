with open ("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART4/file1.txt", "w+") as f:
    f.write("with ka use sikha")
    f.seek(0)
    print(f.read())