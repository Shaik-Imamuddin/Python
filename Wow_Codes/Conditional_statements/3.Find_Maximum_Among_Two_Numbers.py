#Check weather a number is maximum and minimum
a=int(input())
b=int(input())
if a>b:
    print("Maximum",a)
    print("Minimum",b)
else:
    print("Maximum",b)
    print("Minimum",a)

#above method in a single line
a=int(input())
b=int(input())
print(f"Maximum {a}\nMinimum {b}" if a>b else f"Maximum {b}\nMinimum {a}")

#Check weather a number is maximum and minimum
#without using relational operator

a=int(input())
b=int(input())
print("Maximum",(a + b + abs(a - b)) // 2)
print("Minimum",(a + b - abs(a - b)) // 2)


a=int(input())
b=int(input())
print(f"Maximum {(a + b + abs(a - b)) // 2}\nMinimum {(a + b - abs(a - b)) // 2}")

#By using max min inbuilt methods
a=int(input())
b=int(input())
print("Maximum",max(a,b))
print("Minimum",min(a,b))

#By type casting into string and checking with "-"
a=int(input())
b=int(input())
print(f"Maximum {b}\nMinimum {a}" if "-" in str(a-b) else f"Maximum {a}\nMinimum {b}")


a=int(input())
b=int(input())
print(f"Maximum {a}\nMinimum {b}" if "-" not in str(a-b) else f"Maximum {b}\nMinimum {a}")

