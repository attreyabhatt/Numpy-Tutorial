import numpy as np

a = np.array([1,2,3])
print(a)

# Multi-dimension
b = np.array([[10,12,13,14],[21,22,23,24]])

#3d
c = np.array([ [[1,2],[3,4],[9,10]],[[5,6],[7,8],[11,12]]  ])
print(b)
print(c)

#Get dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)

# Get Shape
print(a.shape)
# The outermost dimension will have 2 arrays, each with 4 elements:
print(b.shape)
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
print(c.shape)

# Get Size (count num of elements in whole)
print(a.size)
print(b.size)


