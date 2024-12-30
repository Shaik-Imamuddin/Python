#Input Output Statements

#Output Statements:

#used to print the output ot the console

#To print the output there is a function called  print()


#Syntax:

#print(*objects,sep='',end='',file=sys.stdout,flush=False)


#Objects -> we can give any no.of objects seperated by commas
a,b=10,40
print(a,b)

# sep => is used to print multiple items with a separator

print("python","java","c",sep="||")

#end => by usign end we can change the end charecter
# -> by default the value of end charecter is new line

print("Hello",end=" ")
print("World")

# ->file ->to print the output in other files
#  By default sys.stdout which is nothing but console

# ->flush - > print with a delay between the output 
# default value is false

import time
for i in range(5):
    print(i,end=" ",flush=True)
    time.sleep(1)

# Input statements

#To take the input there is a function called input() function

#if we are passing input By using input function
#every thing will be treated as string

#To take the input in int and float we need to type cast the input by using
#below functions

#input()        ->takes string input
#int(input())      ->takes integer input
#float(input()) ->takes float input
#bool(input())  ->takes boolean input

a = input()
print(a)
print(type(a))

c=int(input())
print(c)
print(type(c))

b=float(input())
print(b)
print(type(b))

d=bool(input())
print(d)
print(type(d))
