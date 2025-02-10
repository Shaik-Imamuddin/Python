#-----find the maximum Element-----

#Taking the list element input and printing the output
#if we are giving only split()
#we have to enter input elements separated by space
l=list(map(int,input().split()))
print(l)

#we can split that by using any other separator
#by giving that as a parameter to the split() method
#in the below method we have to enter input elements separated by commas
l=list(map(int,input().split(",")))
print(l)

#By using max method
l=list(map(int,input().split()))
print(max(l))

#By using sort method
#and accessing the last charecter
l=list(map(int,input().split()))
l.sort()
print(l[-1])

#By using sorted method
#and accessing the last charecter
l=list(map(int,input().split()))
print(sorted(l)[-1]))

#By using list Comprehension
l=list(map(int,input().split()))
print([i for i in l if i == max(l)][0])

#using max along with list comprehension
l=list(map(int,input().split()))
print(max([i for i in l]))

#without using inbuilt methods
l=list(map(int,input().split()))
maximum=l[0]
for i in l:
    if i>maximum:
        maximum=i
print(maximum)

#-----Find the second maximum Element-----

#By using the sorted method in descending order
#And accessing the 2nd index value
l=list(map(int,input().split()))
sl=sorted(l,reverse=True)
print(sl[1])

#Without using sort method
    l = list(map(int, input().split()))
first=second=l[0]
for i in l:
    if i > first:
        second=first
        first = i
    elif i > second and i != first:
        second = i
if second == max(l):
    print("No second maximum exists.")
else:
    print(second)

#-----Find the kth maximum Element-----

#both the methods doesn't support when the list contains of duplicates

#By sorting the list and accessing the last position
l=list(map(int,input().split()))
k=int(input())
if k>len(l) or k<=0:
    print("Invalid value of k")
else:
    sl=sorted(l,reverse=True)
    print(sl[k-1])

#By removing k-1 maximum elements
#and Accessing the kth element
l=list(map(int,input().split()))
k=int(input())
if k>len(l) or k<=0:
    print("Invalid value of k")
else:
    for i in range(k-1):
        l.remove(max(l))
    print(max(l))

#To overcome the problem of duplicates convert the list to set
l=list(map(int,input().split()))
sl=list(set(l))
k=int(input())
if k>len(sl) or k<=0:
    print("Invalid value of k")
else:
    s=sorted(sl,reverse=True)
    print(sl[k-1])
