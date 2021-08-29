import numpy as np

#3d
a = np.array( [[ [1,2],[3,4] ], [ [5,6],[6,7] ] ])

#Get specific element
b = a[0,1,1]
print(b)

# Get the row
b = a[1,0,:]
print(b)