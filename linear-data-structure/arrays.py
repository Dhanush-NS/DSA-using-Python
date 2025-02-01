# Array is collection of elements of same type where stored in a contigous memory location, each element can be accessed usign index and typically the starting of the index is 0

array = [1,2,3,4,5,4,1,3]

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


#function to find the max element in the array
def max_elem(array):
    return max(array)
print(max_elem(array))

#fucntion to reverse an array
def rev_array(array):
    return array[::-1]
print(rev_array(array))

#count occurences
def occ_array(array,elem):
    counter = 0
    for i in array:
        if i == elem:
            counter += 1
    return counter
elem = 3
print(occ_array(array,elem))

#combine the sorted arrays
arr1 = [1,5,3,2,6,4]
arr2 = [8,10,7,9,12]
def sort_arr():
    combined = arr1+arr2
    combined.sort()
    return combined
print(sort_arr()) 



#Remove duplicates in the array
a = [1,2,2,4,5,3,3,5,6,7,2,1]
def array_dup():
    dup = []
    for i in a:
        if i not in dup:
            dup.append(i)
    return dup
print(array_dup())

a=1,4,3,2
def reverse_array():
    a1= a[::-1]
    return a1
print(reverse_array())