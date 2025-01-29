# Array is collection of elements of same type where stored in a contigous memory location, each element can be accessed usign index and typically the starting of the index is 0

array = [1,2,3,4,5]

#append
array.append(6)
print(array)

#insert
array.insert(6,7)
print(array)

#pop
array.pop()
print(array)

#remove
array.remove(5)
print(array)

#traversal
print(array)

#update 
array[0] = 21
print(array) 

#linear search in array
def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
print(linear_search(array,3))