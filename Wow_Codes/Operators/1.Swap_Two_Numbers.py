#Swapping of 2 numbers

#By using temporary variable
a=10
b=20
temp =a
a=b
b =temp
print(a)
print(b)

#using addition and subtraction operators
a=10
b=20
a=a+b   #30
b=a-b   #30-20 ->10
a=a-b   #30 -10 ->20
print(a)
print(b)

#By interchanging the variables
a=10
b=20
a,b=b,a
print(a)
print(b)

# By using Bitwise XOR operator
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#by using multiplication and Division operators
a=10
b=20
a=a*b   #200
b=a//b  # 200//10 => 20
a=a//b  # 200//20 => 10
print(a)
print(b)
