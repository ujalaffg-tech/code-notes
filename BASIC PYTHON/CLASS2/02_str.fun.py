
# .endswith(" ")
str1 = " I am studing python from Apnacollege"
print(str1.endswith("ege"))         
print(str1.endswith("age"))

# .capitalize()
str2 = "i am studing python from apna collage "         
print(str2.capitalize()) 
print(str2)
# ye sirf pahla alphabate ko capitalaze karta hain 
# aur ha ak hi bar ab fir se print karoge
# to normal hi print hoga 
# variable se karoge to change nahi hoga
str2 =  str2.capitalize()
print(str2)

# .replace(" " , " ")
print(str2.replace("a" , "s"))          
print(str2.replace("python" , "java"))

# .find("     ")
print(str2.find("o"))
print(str2.find("python"))
print(str2.find("q")) 
#:ager koi letter exist nahi then -1 print hoga         

# .count("    ")
print(str2.count("a"))
print(str2.count("apnacollage"))
