import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100, 100, 10)
dx, dy = np.meshgrid(axes_values, axes_values)
print('dx', dx)
print('dy', dy)

function = 2 * dx + 3 * dy

function2 = np.cos(dx) + np.cos(dy)

print(function)

plt.imshow(function)
plt.title('function of plot 2*dx + 3 * dy')
plt.colorbar()
plt.savefig('myfig.png')

plt.imshow(function2)
plt.title('function cos plot')
plt.colorbar()
plt.savefig('function_cosfig.png')