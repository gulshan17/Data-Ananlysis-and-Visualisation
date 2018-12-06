import numpy as np
arr = np.arange(0, 12)
print('array = \n', arr)
#print('array[0] = \n', arr[0])
array2 = arr[0 : 5]
#print('array2 = \n', array2)
#print('array = \n', arr)

arr[0 : 5] = 17
print('array = \n', arr)
arr2 = arr[0 : 6]
print(arr2)

arr2[:] = 29
print(arr2)

print(arr)
#in numpy if we assign the slice of an array, they basically point to the same locatino

#to create a new array copy with different memory
arrcopy = arr.copy()
print(arrcopy)