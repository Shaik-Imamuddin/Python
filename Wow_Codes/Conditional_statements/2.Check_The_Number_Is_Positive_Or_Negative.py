#Check the Given number is positive or negative

#By using condition with relational Operators
n=int(input())
if n>0:
    print("Positive")
else:
    print("Negative")

#1st method in single line 
n=int(input())
print("Positive" if n>0 else "Negative")

#Check the Given number is positive or negative without using relational operators

#By type-casting into string and checking condition along with not in operator
n=int(input())
print("Positive" if "-" not in str(n) else "Negative")

#By type-casting into string and checking condition along with in operator
n=int(input())
print("Negative" if "-" in str(n) else "Positive")
