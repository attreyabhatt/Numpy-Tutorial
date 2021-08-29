import numpy as np

a = np.array([1,2,3])

#2d
b = np.array([[10,12,13,14],[21,22,23,24]])

#3d
c = np.array([ [[1,2],[3,4],[9,10]],[[5,6],[7,8],[11,12]]  ])

# Get specific element [r,c]
print(b[0,2])

# Get specific row [r,:]
print(b[1,:])

# Get only specific elements with steps [row, startindex:endindex+1:stepsize]
print(b[1,1:4:2])

#Get specific element in 3d
b = a[0,1,1]
print(b)

# Get the row in 3d
b = a[1,0,:]
print(b)

