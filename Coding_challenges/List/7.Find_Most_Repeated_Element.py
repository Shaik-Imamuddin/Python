#-----Find the most repeated element-----

#Write a python program to Find the most repeated element

#Sample Test cases
#Input
#1 2 3 2 2 1 4 2 5 2 3 2
#output
#2


#By using loops and conditions
l = list(map(int, input().split()))
most_repeated = None
max_count = 0
for i in range(len(l)):
    count = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1
    if count > max_count:
        max_count = count
        most_repeated = l[i]
print(most_repeated)


#By comparing the count of Each and Every Element in an array
l = list(map(int, input().split()))
l.sort()
most_repeated = l[0]
max_count = 1
current_count = 1
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            most_repeated = l[i - 1]
        current_count = 1
if current_count > max_count:
    most_repeated = l[-1]
print(most_repeated)

#By using key attribute
l = list(map(int, input().split()))
print(max(l, key=l.count))


#By using mode method statistics module
import statistics
l = list(map(int, input().split()))
print(statistics.mode(l))

