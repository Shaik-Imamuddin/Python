#-----Find the Minimum Element-----

# Taking the list element input and printing the output
# If we are giving only split(), enter input elements separated by space
l = list(map(int, input().split()))
print(l)

# We can split using a different separator by specifying it in the split() method
# Below, enter input elements separated by commas
l = list(map(int, input().split(",")))
print(l)

# By using the min() method
l = list(map(int, input().split()))
print(min(l))

# By using the sort() method and accessing the first character
l = list(map(int, input().split()))
l.sort()
print(l[0])

# By using the sorted() method and accessing the first character
l = list(map(int, input().split()))
print(sorted(l)[0])

# By using list comprehension
l = list(map(int, input().split()))
print([i for i in l if i == min(l)][0])

# Using min() along with list comprehension
l = list(map(int, input().split()))
print(min([i for i in l]))

# Without using inbuilt methods
l = list(map(int, input().split()))
minimum = l[0]
for i in l:
    if i < minimum:
        minimum = i
print(minimum)

#-----Find the Second Minimum Element-----

# By using the sorted() method in ascending order and accessing the second element
#it will possible if the list contains duplicates also
l = list(map(int, input().split()))
sl = sorted(list(set(l)))
print(sl[1])

# Without using the sort() method
#it will be possible only in some cases if the list contains duplicates
l = list(map(int, input().split()))
ul=list(set(l))
first = second = ul[0]
for i in ul:
    if i < first:
        second = first
        first = i
    elif i < second and i != first:
        second = i
if second == min(ul):
    print("No second minimum exists.")
else:
    print(second)

#-----Find the Kth Minimum Element-----

#finding Minimum element is not possible for first 2 methods if the list contains duplicates
# By sorting the list in ascending order and accessing the k-1 index value
l = list(map(int, input().split()))
k = int(input())
if k > len(l) or k <= 0:
    print("Invalid value of k")
else:
    sl = sorted(l)
    print(sl[k - 1])

# By removing k-1 minimum elements and accessing the kth element
l = list(map(int, input().split()))
k = int(input())
if k > len(l) or k <= 0:
    print("Invalid value of k")
else:
    for i in range(k - 1):
        l.remove(min(l))
    print(min(l))

# To overcome the problem of duplicates, convert the list to a set
l = list(map(int, input().split()))
sl = list(set(l))
k = int(input())
if k > len(sl) or k <= 0:
    print("Invalid value of k")
else:
    s = sorted(sl)
    print(s[k - 1])
