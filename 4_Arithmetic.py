#Some arithmetic rules to remember
cats = 10
dogs = 8
rabbits = 4
tucans = 20
hogs = 7
doves = 3

#These pairs do the same thing
cats = cats + 1
cats += 1

dogs = dogs - 1
dogs -= 1

rabbits = rabbits * 2
rabbits *= 2

tucans = tucans / 2
tucans /= 2

hogs = hogs **2
hogs **= 2

#For remainders
remainder = doves % 2
#This can be used to see if a number is odd or even

#print(cats, dogs, rabbits, tucans, hogs, doves)
#print(type(cats))
#print(remainder)

x = 3.14
y = -4
z = 5

r1 = round(x)
r2 = abs(y)
r3 = pow(16, 2)
r4 = max(x, y, z)
r5 = min(x, y, z)

print(r1, r2, r3, r4, r5)

import math
print(round(math.pi, 3))
# For specifics, you can use 'from math import sqrt, pi' then simply use the word sqrt instead of math.sqrt

#to round up:
a= math.ceil(x)
#to round down:
b= math.floor(x)
print(a, b)

newx = 5
newx = newx/2
print(newx)