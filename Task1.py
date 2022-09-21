# this block import necessary library and use the loop to generate 100 random numbers
import random
randomlist = []
for i in range(0, 100):
    n = random.randint(1, 1000)
    randomlist.append(n)
#print(randomlist)

# new empty list created, the first value from randomList is compared with the entire list and finds the minimum,
# this number is added to the new list and removed from the old one,
# then the same cycle continues till randomList has values
randomSortedList = []
while randomlist:
    minimum = randomlist[0]
    for value in randomlist:
        if value < minimum:
            minimum = value
    randomSortedList.append(minimum)
    randomlist.remove(minimum)
#print(randomSortedList)

# loop iterates over the values in the sorted list, count even and odd numbers and their sums
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
for val in randomSortedList:
    if val % 2 == 0:
        even_sum += val
        even_count += 1
    elif val % 2 != 0:
        odd_sum += val
        odd_count += 1
#print (even_sum, even_count, odd_sum, odd_count)

# expressions for calculating the average values
# if count of values is 0, there are exception for that
try:
   even_avg = even_sum / even_count
   odd_avg = odd_sum / odd_count
   print("Even average is", int(even_avg), "and", "Odd average is", int(odd_avg))
except ZeroDivisionError:
    print("Error, you are dividing by zero")