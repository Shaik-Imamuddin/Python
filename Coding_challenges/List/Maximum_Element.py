#Find the second maximum Element
l=list(map(int,input().split()))
sl=sorted(l,reverse=True)
print(sl[1])

#Find the kth maximum Element

l=list(map(int,input().split()))
k=int(input())
if k>len(l) or k<=0:
    print("Invalid value of k")
else:
    sl=sorted(l,reverse=True)
    print(sl[k-1])


