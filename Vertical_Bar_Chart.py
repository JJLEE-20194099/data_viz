import numpy as np
import matplotlib.pyplot as plt;

linear_data = np.array([1, 2, 3, 4, 5, 6])
exponential_data = linear_data ** 2;

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)

exp_xvals = [];
for item in xvals:
    exp_xvals.append(item + 0.3)

plt.bar(exp_xvals, exponential_data, width=0.3, color='r')

plt.legend(['Linear Data', 'Exponential Data'])
plt.show()