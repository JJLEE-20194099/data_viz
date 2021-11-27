import numpy as np
import matplotlib.pyplot as plt;

linear_data = np.array([1, 2, 3, 4, 5, 6])
exponential_data = linear_data ** 2;

xvals = range(len(linear_data))
plt.plot(xvals, linear_data, '-o')

plt.plot(xvals, exponential_data, '-x')
plt.gca().fill_between(xvals, linear_data, exponential_data, facecolor = 'blue')

plt.legend(['Linear Data', 'Exponential Data'])
plt.show()