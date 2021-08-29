import numpy as np

# Initialize zeros
a = np.zeros(5)
b = np.zeros((2,3))

# Initialize ones
c = np.ones((3,2))

# Any other number (shape,number,dtype=optional)
d = np.full((2,2),99,dtype='float32')
e = np.full_like(a,4)
print(e)
# Evenly spaced numbers (startingnum,endnum, num=number of numbers needed,dtype=optional)
a = np.linspace(10,20,num=10,dtype='int32')

# Create an array with increasing steps
a = np.arange(1,10,2)

# Random decimal numbers (shape)
r = np.random.rand(2,2)

# Random integer numbers (startRand,endRand+1, size=shape)
rint = np.random.randint(4,10,size=(3,3))

# The identity Matrix
iden = np.identity(5)

# Repeating (make array 2-dim then repeat)
a = np.array([[1,2,3]])
rep = np.repeat(a,3,axis=0)

