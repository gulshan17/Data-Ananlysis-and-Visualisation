import numpy as np
from numba import vectorize

x = np.array([100, 400, 500, 600])
y = np.array([10, 15, 20, 25])
condition = np.array([True, True, False, False])

#use loops indirectly
#z = [a if cond else b for a, cond, b in zip(x, condition, y)]
#print(z)

#simpler version for above code using numpy
#np.where(#condition, #value for yes, # value for no)

#z2 = np.where(condition, x, y)
#print(z2)

x = np.array([0, 17, 21, 0, 8, 1])
#print('x = \n', x)
z3 = np.where(x > 0, 0, 17)
#print('np.where(x > 0, 0 , 17) = \n', z3)

#Standard function of numpy

#sum x
#rint(x.sum())

#column sum
#print(x.sum(0))

n = np.array([[1, 2], [3, 4]])
print('array = \n', n)
print('array.sum() = \n', n.sum(0))

print('array = \n', x)
print('array.mean() = \n', x.mean())

print('array.std() = \n', x.std())

print('array.var() = \n', x.var())

#logical operations
condition2 = np.array([True, False, True])
print('condition_array = \n', condition2)
print('condition_array.any() = \n', condition2.any())
print('condition_array.all() = \n', condition2.all(0))

unsorted_array = np.array([1, 17, 3, 12, 34, 34])
print(unsorted_array.sort())
print('unsorted_array = \n', unsorted_array)
print('sorted_array = \n', unsorted_array)

arr2 = np.array(['solid', 'solid', 'solid', 'liquid', 'liquid', 'gas', 'gas'])
print('array = \n', arr2)
print('numpy.unique(array) = \n', np.unique(arr2))

print(np.in1d(['solid', 'gas', 'plasma'], arr2))

