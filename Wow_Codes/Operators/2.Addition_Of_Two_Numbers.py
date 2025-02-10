#Addition of 2 numbers

#By using Addition operator (+)
a = int(input())
b = int(input())
print(a+b)

#Without using Addition operator
a=int(input())
b=int(input())
print(a-(-b))

#By using bitwise operators
a=int(input())
b=int(input())
while b!=0:
    carry = a&b
    a=a^b
    b=carry<<1
print(a)

#By using functions
def sum(a,b):
    print(a+b)
a=int(input())
b=int(input())
sum(a,b)

#By using compound assignment
a=int(input())
b=int(input())
a+=b
print(a)

#By using the sum inbuilt method in lists
a=int(input())
b=int(input())
print(sum([a,b]))

#By using the inbuilt method in operator module
import operator
a=int(input())
b=int(input())
print(operator.add(a,b))
