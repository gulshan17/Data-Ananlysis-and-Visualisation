import numpy as np

print(np.array([1, 2]))

my_list1 = [1, 2, 3, 4]
my_array1 = np.array(my_list1)

print(my_array1)

my_list2 = [5, 6, 7, 8]
my_array = np.array([my_list1, my_list2])
print(my_array)

# usage of shape function
print(my_array.shape)

# finding the datatype of members of the array
print(my_array.dtype)

#zeros, ones, empty, eye, arange
new_array1 = np.zeros([5, 4])
print(new_array1)

print(np.ones([5, 5]))




print(np.eye(5))

#arraange function
new_array3 = np.arange(5, 85, 17)
print(new_array3)

new_array2 = np.empty(5)

print(new_array2)