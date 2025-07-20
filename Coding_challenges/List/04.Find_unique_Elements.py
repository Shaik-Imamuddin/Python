#-----Find the Unique Elements or the elements repeated only once-----

#Write a python program to find the Unique elements
#or the elements repeated only once in a list

#Sample Test cases

#Input
#1 2 3 4 1 2 4 5
#output
#[3,5]

#By Comparing values using in and not in
#and adding the Unique elements into an array  
l=list(map(int,input().split()))
seen = []
dups = []
unique=[]
for i in l:
    if i not in seen:
        seen.append(i)
    elif i not in dups:
        dups.append(i)
for i in seen:
    if i not in dups:
        unique.append(i)
print(unique)

#By using list Comprehension along with lists
l=list(map(int,input().split()))
seen = []
dups = []
for i in l:
    if i not in seen:
        seen.append(i)
    elif i not in dups:
        dups.append(i)
print([i for i in seen if i not in dups])

#By using set and comparing values 
l = list(map(int, input().split()))
seen = set()
dups = set()
for n in l:
    if n in seen:
        dups.add(n)
    seen.add(n)
print(list(seen - dups))

#By using list comprehension along with count() method
l = list(map(int, input().split()))
unique = [i for i in l if l.count(i) == 1]
print(unique)

#By using set comprehension and changing the type to lists
l = list(map(int, input().split()))
unique = list({x for x in l if l.count(x) == 1})
print(unique)

#By using enumarate() function
l = list(map(int, input().split()))
print([i for n, i in enumerate(l) if l.count(i) == 1])
