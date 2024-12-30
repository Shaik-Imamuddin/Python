#variables

# a variable is a name which is given to memory location
# which will stores the value temporarily


#single assignment
a=100
print(a)
s='string'
print(s)

#multiple assignment
b,c=200,'python'
print(b)
print(c)
print(a,b,c,s)

#single value to multiple variables
a=b=c=5000    
print(a)    
print(b)    
print(c)
print(type(b)) #int

# if we are assigning  multiple values to a single variable 
# it should be treated as tuple
a=120,240,560
print(a)
print(type(a))  #tuple

b=345,
print(b)
print(type(b))  #tuple
