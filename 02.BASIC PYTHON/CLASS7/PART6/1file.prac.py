'''Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
we are learning File 1/O
using python.
I like programming in Java.'''
with open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART6/2practice.txt", "w+")as f:
    f.write("Hi everyone \nwe are learning File 1/0 using python ") ## n sikho "\n"
    f.write("\nI like programming in Java.")
    f.seek(0)
    print(f.read())

#| WAF that replace all occurrences of "java" with "python" in above file.
def replace(a,b):
    with open ("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART6/2practice.txt","r+") as f:
        data = f.read()
        data = data.replace(a,b)
        f.seek(0)
        f.write(data)
        f.seek(0)
        print(f.read())
replace("Java","python")

#- Search if the word "learning" exists in the file or not.
def check(x):
    with open ("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART6/2practice.txt","r+") as f:
        data = f.read()
        if(data.find(x) == -1):
            print("i dont find it.")
        else:
            print("i found it")
check("leearning")

#| WAF to find in which line of the file does the word "learning" occur first.
#| Print -1 if word not found.
def found(x):
    with open("/Users/adityakumarsingh/VS CODE PYTHON/BASIC PYTHON/CLASS7/PART6/2practice.txt","r+")as f:
        data = f.readlines() ## file ka har line list me
        idx = 1
        for val in data:
            if x in val:
                return idx
            idx += 1
        return -1
print(found("learning"))