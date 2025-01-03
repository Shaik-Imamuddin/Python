#How to print strings to console

print("Hello wolrd")

#print hello world in next line
print("Hello\nWolrd")

#print hello world in single line along with escape sequence
#This is called a raw string
print(r"Hello\nWolrd")

a=10
# if we are separating the string and variable using comma(,)
#it will print a space by default
print("The value of a is",a)

#if you dont want spaces use concatination

# we cant add a string and integer so we have done type casting
print("The value of a is"+str(a))

# By using format strings we can print that without spaces

#if we are using format strings 
#then use variable names in flower braces
#1st way to use format strings
print(f"The value of a is{a}")

#2nd way to use format strings
print("The value of a is {}".format(a))

print("The value of a is {0}".format(a))

# if we are printing more than a value then we can pass 
# that much no.of arguments we need to pass in format method
a=10
b=20
print("The value of a={} and b={}".format(a,b))
print("The value of a={} and b={}".format(b,a))
print("The value of a={1} and b={0}".format(b,a))
print("The value of a={0} and b={1}".format(b,a))
#print("The value of a={a} and b={b}".format(a,b))#key Error
print("The value of a={a} and b={b}".format(a=a,b=b))

#By using format specifiers
print("The value of a=%d and b=%d"%(a,b))
