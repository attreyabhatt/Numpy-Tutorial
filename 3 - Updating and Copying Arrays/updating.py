import numpy as np

a = np.array([1,2,3])
print(a)

# Multi-dimension
b = np.array([[10,12,13,14],[21,22,23,24]])

# Change epecific element
print('Change specific element')
b[0,2] = 100  
print(b)

# Change whole row,column
# b[0,:] = [1,1,1,5]
b[0,:] = 2
print(b)