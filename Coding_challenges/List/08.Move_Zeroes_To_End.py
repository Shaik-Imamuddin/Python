#By Taking a new list 
# and adding non_zero elements first
# later will add the zeroes

arr = list(map(int, input().split()))
res = []
for i in arr:
    if i != 0:
        res.append(i)
for i in arr:
    if i == 0:
        res.append(0)
for i in res:
    print(i,end=" ")


#By interchanging the non_zero elements to Front of list
#Two pointer Approcah
l=list(map(int,input().split()))
index=0
for i in range(len(l)):
    if l[i]!=0:
        l[index],l[i]=l[i],l[index]
        index+=1
for i in l:
    print(i,end=" ")

#By interchanging the non_zero elements to Front of list
#Two pointer Approcah(using while loop)
arr = list(map(int, input().split()))
i = 0
j = 0
while i < len(arr):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
for i in arr:
    print(i,end=" ")

#Using list comprehension
#storing the non zero elements in a lsit and Non zero elements in another list
#at the end merging the 2 lists
l = list(map(int, input().split()))
non_0 = [x for x in l if x != 0]
noof_0=[0]*(len(l)-len(non_0))
l = non_0+noof_0
for i in l:
    print(i,end=" ")