
#~ list me sab kuch store hoga dict.....
marks = [69.69, 70.04, 55.81, 99.99, 67,78]
print(marks) 
print(type(marks))
print(len(marks))

#it can store (int, float, string, dict etc)
student =  ["aditya", 69, "patna"]
print(student)

#: empty list
x = []

#: ye mutable hain
student[0] = "prince"  
print(student)         

#.index
print(marks[0])
print(marks[4])

#.slicing
marks = [69, 98 ,78 ,50]
print(marks[1:3])
print(marks[:3])
print(marks[3:])
# print(marks[-1:-3])
print(marks[-3])
print(marks[-3:-1])

#-methods
#.reverse()
digit = [2,5,8,6,1,9]
digit.reverse()
print(digit)
#.append()
digit.append(3)
print(digit)
#.insert()              
#:(index , element)     element ko index ke hisab se rakhega
digit.insert(1 , 0)
print(digit)
#.remove()
digit.remove(8)         #jo ank daloge o hat jayega
print(digit)
#.pop()
digit.pop(0)            #: ye index ke hisab se remove karega
print(digit)
#.sort 
# #: #assending order                 
numbers = [3,1,5,2]
numbers.sort()
print(numbers)
#.sort(reverse = True)
#:dessending ke liye      
numbers.sort(reverse = True)
print(numbers)