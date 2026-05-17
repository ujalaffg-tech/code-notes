
#| From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART6/4practice2.txt", "r+")as f:
    data = f.read()
    newdata = data.split(",")
    for val in newdata:
        if(int(val) % 2 == 0):
            count += 1
print(count)
              

