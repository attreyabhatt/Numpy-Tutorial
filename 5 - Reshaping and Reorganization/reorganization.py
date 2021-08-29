import numpy as np

# Reshaping a matrix

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

## Make sure the aftershapedim1 * aftershapedim2 * ... = row * columns of beforematrice
## (other wise there is a mismatch in shape and error occurs)

after = before.reshape(8,1)
print(after)

# Vertically stacking vectors/arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

v3 = np.vstack([v1,v2,v1,v1,v2])

# Horizontal stacking vectors/arrays
v4 = np.hstack([v1,v2])

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(h1)
print(h2)

h3 = np.hstack([h1,h2])

print(h3)

