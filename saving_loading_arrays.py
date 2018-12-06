import numpy as np

arr = np.arange(1, 17)
print(arr)

np.save('saved_arr', arr)

arr1 = np.load('saved_arr.npy')
print(arr1)

#save multiple arrays
arr2 = np.arange(25)
arr3 = np.arange(34)

np.savez('save_archive.npz', x = arr2, y = arr3)

load_array = np.load('save_archive.npz')

print(load_array['x'])
print(load_array['y'])

#save array to text file

np.savetxt('textfile.txt', arr1, delimiter = ' ')

#load txt files
load_txt_arr = np.loadtxt('textfile.txt', delimiter= ' ')
print(load_txt_arr)

