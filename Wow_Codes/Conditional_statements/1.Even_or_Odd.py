#By using modulus operator
n=int(input())
if (n%2)==0:
    print("Even")
else:
    print("Odd")

#By using ternary in a single line
n = int(input())
print("Even" if n % 2 == 0 else "Odd")


#By using Bitwise and (&) and comparing with 0
n=int(input())
if (n&1)==0:
    print("Even")
else:
    print("Odd")

#By using Bitwise and (&) and directly executing true statements
n=int(input())
if (n&1):
    print("Odd")
else:
    print("Even")

#By using bitwise XOR
n = int(input())
if (n^1)==n+1:
    print("Even")
else:
    print("Odd")

#by converting number into binary and checking with last bit
n = int(input())
binary = bin(n)
print("Even" if binary[-1] == '0' else "Odd")


#By using floor division and multiplication 
n=int(input())
if ((n//2)*2==n):
    print("Even")
else:
    print("Odd")

#By using normal division along with floor() method
import math
n = int(input())
if math.floor(n / 2) * 2 == n:
    print("Even")
else:
    print("Odd")

#By converting it into string
n = int(input())
if str(n)[-1] in ['0', '2', '4', '6', '8']:
    print("Even")
else:
    print("Odd")

#By using list indexing
#insted of [n%2] we can use any other expression with returns 0 and 1
n = int(input())
print(["Even", "Odd"][n % 2])
