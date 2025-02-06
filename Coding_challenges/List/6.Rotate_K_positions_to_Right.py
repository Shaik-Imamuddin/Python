#-----Rotate K positions to right-----

#Write a python program to rotate K positions to right

#Sample Test cases
#Input
#1 2 3 4 5
#2
#output
#[4, 5, 1, 2, 3]

#By storing the value in another value
#and shifting it to front
#Simply by using swapping logic
lst = list(map(int, input().split(' ')))
k = int(input())
for i in range(k):
    temp = lst[-1]  
    for j in range(len(lst) - 1, 0, -1):  
        lst[j] = lst[j - 1]
    lst[0] = temp 
for i in lst:
    print(i, end=" ")

#By using slicing
arr = list(map(int, input().split()))
k = int(input())
k = k % len(arr)
print(arr[-k:] + arr[:-k])
print("-----------------------")

#By using List Comprehension along with Looping Statements
arr = list(map(int, input().split()))
k=int(input())
print([arr[(i - k) % len(arr)] for i in range(len(arr))])

#By using Looping Statements
arr = list(map(int, input().split()))
k = int(input())
k = k % len(arr)
for i in range(0, k):
    arr = [arr[-1]] + arr[0:-1]
print(arr)

#By using list comprehension along with Looping Statements
arr = list(map(int, input().split()))
k = int(input())
l=len(arr)
print([arr[(i-k)%l] for i in range(l)])

#By using slicing
arr = list(map(int, input().split()))
k = int(input())
print(arr[-k % len(arr):] + arr[:-k % len(arr)])

#By Using slicing along with conditional statement
arr = list(map(int, input().split()))
k = int(input())
print(arr[-k%len(arr):]+arr[:-k%len(arr)] if k%len(arr)!=0 else arr)
