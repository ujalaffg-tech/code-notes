
#~ tupple me sab kuch store hoga
digits = (2,4,6,7,3,)      #:multiple elements ho tab comma optional hai
print(type(digits))
print(digits)

#: empty tupple
t = ()
print(type(t))

#: yah immutable hai
# t = (1,2,3,)
# t[0] = 2
# print(t)              error

#. index
print(digits[0])
print(digits[-3])

#. slicing
print(digits[2:4])

#.methods
digits = (2,3,5,7,2,9,2)
print(digits.index(9))      # jo ank daloge o kaha hai pata chalega
print(digits.count(2))

#.negative slicing
print(digits[-3:-2])