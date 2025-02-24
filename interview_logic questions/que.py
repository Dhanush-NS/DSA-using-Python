# Find the missing numbers

def miss_numbers(num):
   start = min(num)
   end = max(num)
   total_sum = sum(range(start,end +1))
   arr_sum = sum(num)
   return total_sum - arr_sum
num = [1,2,4,5,6]
print(miss_numbers(num))


# merge two strings
from itertools import zip_longest
name1 = "dhanush"
name2 = "punith"
res = list(zip_longest(name1,name2,fillvalue="null"))
print(res)


name1 = "dhanush"
name2 = "punithm"
for i in range(len(name1)):
    r = (name1[i],name2[i])
    print(r)