#-----Rotate K positions to left-----

#Write a python program to rotate K positions to left

#Sample Test cases
#Input
#1 2 3 4 5
#2
#output
#[3, 4, 5, 1, 2]

#By storing the value in another value
#and shifting it to end
#Simply by using swapping logic
lst = list(map(int,input().split(' ')))
k = int(input())
for i in range(k):
    temp = lst[0]
    for j in range(len(lst)-1):
        lst[j] = lst[j+1]
    lst[-1] = temp
for i in lst:
    print(i,end=" ")

#By using looping statement
arr = list(map(int, input().split()))
k = int(input())
k = k % len(arr)
for i in range(k):
    arr = arr[1:] + [arr[0]]
print(arr)

#By using list comprehension along with Looping Statements
arr = list(map(int, input().split()))
k = int(input())
l = len(arr)
print([arr[(i + k) % l] for i in range(l)])


#By using Sclicingdirectly by dividing with length
arr = list(map(int, input().split()))
k = int(input())
print(arr[k % len(arr):] + arr[:k % len(arr)])


#By using slicing
lst = list(map(int,input().split(' ')))
k = int(input())
k = k % len(lst)
print(lst[k:] + lst[:k])


#By using slicing along with conditions
lst = list(map(int,input().split(' ')))
k = int(input())
print(lst[k%len(lst):]+lst[:k%len(lst)] if k%len(lst)!=0 else lst)
