import numpy as np
from numpy.lib.function_base import percentile


a = np.array([[1,2],[3,4]])

# Be careful while copying
# b = a
# b[0,0] =100
# print(a)

b = a.copy()
b[0,0] =100
print(a)
print(b)
