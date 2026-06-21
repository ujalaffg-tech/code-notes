
#- Store following word meanings in a python dictionary:
''' table: "a piece of furniture", "list of facts & figures"
 cat : "a small animal" '''
dict = {"table":["a piece of forniture","list of fact 7 figures"],
        "cat":"a small animal"}
print(dict)

#-You are given a list of subjects for students. 
'''Assume one classroom is required for 1 subject. 
How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript"?
"java", "python", "java", "C++", "C" '''

subjects = {"python", "java", "C++", "python", "javascript"
"java", "python", "java", "C++", "C" }
result = len(subjects)
print("no of classroom",result)

#| WAP to enter marks of 3 subjects from the user and store 
'''them in a dictionary. Start with an empty dictionary 
& add one by one. Use subject name as key & marks as value.
 '''
dict1 = {}
marks1 = int(input("enter marks 1 : "))
marks2 = int(input("enter marks 2 : "))
marks3 = int(input("enter marks 3 : "))
dict1["mark1"] = marks1
dict1["mark2"] = marks1
dict1["mark3"] = marks1
print(dict1)

'''Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)'''
set = {9,"9.0"}
print(set)

