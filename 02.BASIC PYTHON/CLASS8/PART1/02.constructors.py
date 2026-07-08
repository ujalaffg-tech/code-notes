
#.constructors
class Students:
    ## default constructors
    def __init__(self):
        print("hello")

    ## parameterized constructors
    def __init__(self,name,marks):
                ## arguments
        self.name = name 
        self.marks = marks
        #: jab har obj me name alag alg ho tab self.name ka use karte hain
        #: example ke liye har student ka name alag alg hoga

s3 = Students("karan",97)
print(s3.name,s3.marks)