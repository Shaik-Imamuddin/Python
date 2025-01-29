#-----find the Duplicate or Repeated Elements-----

#Write a python program to find the duplicate elements From the list

#Sample Test cases

#Input
#1 2 3 4 1 2 4 5
#output
#[1,2,4]


#By storing the Unique values in one list
#And Duplicate values in another list
l=list(map(int,input().split()))
seen = []
dups = []
for i in l:
    if i not in seen:
        seen.append(i)
    elif i not in dups:
        dups.append(i)
print(dups)


#By using set method to store only Unique elements
#And another set to return duplicates
l=list(map(int,input().split()))
seen = set()
dup = set()
result = []
for n in l:
    if n in seen and n not in dup:
        result.append(n)
        dup.add(n)
    seen.add(n)
print(result)

#By using Nested Conditons
l=list(map(int,input().split()))
dup=[]
for i in l:
    if l.count(i)>1:
        if i not in dup:
            dup.append(i)
print(dup)


#By using set comprehension along with set method
l=list(map(int,input().split()))
dup = list({x for x in l if l.count(x) > 1}) #set
print(dup)

#By using enumerate() function
l=list(map(int,input().split()))
print([i for n, i in enumerate(l) if l[:n].count(i) == 1])
