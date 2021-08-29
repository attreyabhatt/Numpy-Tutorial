import numpy as np

## Linear Algebra

# Matrix Multiplication
a = np.ones((2,3))
b = np.full((3,2),2)
c = np.matmul(a,b)

print(a)
print(b)
print(c)

# Find the determinant
a = np.identity(3)
np.linalg.det(a)

## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

## Solving a Linear Equation Example (look for equation.png )

# define matrix A using Numpy arrays
A = np.array([[2, 1, 1],
 [1, 3, 2],
 [1, 0, 0]]) 

#define matrix B
B = np.array([4, 5, 6]) 

# linalg.solve is the function of NumPy to solve a system of linear scalar equations
sol = np.linalg.solve(A,B)
print(sol)