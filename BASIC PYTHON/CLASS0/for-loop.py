'''ANDAR wala PEHLE poora khatam hota hai
TAB bahar wala aage badhta hai'''
#.
a = [1,2,3]
b = [10,20,30]
for x in a:        # a mein 3 elements → 3 baar
    for y in b:    # b mein 3 elements → 3 baar
        print()    # 3×3 = 9 baar
#.
for x in a:          # LOOP 1
    for y in b:      # LOOP 2
        print()      # LOOP 1 + LOOP 2 = 3×3 = 9 baar
#.
for x in a:          # LOOP 1
    for y in b:      # LOOP 2
        pass
    print()          # sirf LOOP 1 = 3 baar
#.
for x in a:          # LOOP 1
    for y in b:      # LOOP 2
        pass
print()              # koi loop nahi = 1 baar

#-1
a = [1,2,3]
b = [10,20,30]
for x in a:
    for y in b:
        print(x,y)

#-2
a = [1,2,3]
b = [10,20,30]
c = [100,200]
for x in a:
    for y in b:
        for z in c:
            print(x,y,z)
        
#-3
a = [1,2,3]
b = [10,20,30]
for x in a:
    for y in b:
        print(x,y)
    print("done",x)

#-4
a = [1,2,3]
b = [10,20,30]
for x in a:
    print("start",x)
    for y in b:
        print(x,y)
        print("..")
    print("done",x)

#-5
a = [1,2,3,4,5]
b = [10,20,30]
for x in a:
    for y in b:
        if y==20:
            print(x,y)

#-6
a = [1,2,3,4,5]
b = [10,20,30]
for x in a:
    for y in b:
        if x==2 or y==30:
            print(x,y)

#-7
a = [1,2,3]
b = [10,20,30]
for x in a:
    for y in b:
        pass
print('end')

#-8
a = [1,2,3]
b = [10,20,30]
for x in a:
    print("x",x)
    for y in b:
        pass
    print(y,"done")
print('all done')

#-9
a = [1, 2, 3]
b = [10, 20, 30]
for x in a:
    for y in b:
        print(x, y)
    print("---")
print("END")

#-10
a = [1, 2, 3]
b = [10, 20, 30]
for x in a:
    for y in b:
        if x == y:
            print(x, y)
    print("checked", x)

#-11
a = [1, 2, 3]
b = [10, 20, 30]
for x in a:
    print("start", x)
    for y in b:
        if y > 15:
            print(x, y)
        print("---")
    print("done", x)
print("END")

#.
'''Kaam:
Har student ke liye batao ki
kitne marks 50 se zyada hain'''
students = ["Ali", "Sara", "Raj"]
marks = [35, 72, 45, 90, 58]
for val in students:
    count = 0
    for i in marks:
        if i>50:
            count+=1
            print(val,"-",count)

students = ["Ali", "Sara", "Raj"]
marks = [35, 72, 45, 90, 58]
for val in students:
    count = 0
    for i in marks:
        if i>50:
            count+=1
        print(val,"-",count)

students = ["Ali", "Sara", "Raj"]
marks = [35, 72, 45, 90, 58]
for val in students:
    count = 0
    for i in marks:
        if i>50:
            count+=1
    print(val,"-",count)
