
#- store the above values in a list & sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

#- WAP to count the number of students with the "A" grade in the following tuple.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#| WAP to check if a list contains a palindrome of elements.
list1 = [1,2,3,2,1]
x = list1.copy()
x.reverse()
if x == list1:
    print("palindrome")
else:
    print("not palindrome")

    
#| WAP to ask the user to enter names of their
#| 3 favorite movie & store them in a list 
movies = []
movie1 = input("enter your first favorite movie : ")
movie2 = input("enter your second favorite movie : ")
movie3 = input("enter your third favorite movie : ")
movies.insert(1,movie1)
movies.insert(2,movie2)
movies.insert(3,movie3)
print(movies)## direct append se bana sakte the fully direct

