#Name: Swetha Susan George
#Id: X123932

import numpy as np
from numpy import matrix
from numpy import random

#Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
A = matrix(random.random(15).reshape(3,5))
print("Matrix A:\n",A)

#Find the size and length of matrix A
size_A = A.size
length_A = len(A)
print("\nSize of A:",size_A)
print("\nLength of A:",length_A)

#Resize (crop/slice) matrix A to size (3,4)
A = A[:,:4]
print("\nResized A(3,4):\n",A)
print("New shape of A:",A.shape)

#Find the transpose of matrix A and assign it to B
B = A.T
print("\nMatrix B:\n",B)

#Find the minimum value in column 1 of matrix B (check the properties of a matrix – ‘B.min()’)
min_col = B[:,0].min()
print("\nMinimum value of column 1 of matrix B:",min_col)

# Find the minimum and maximum values for the entire matrix A
min_A = A.min()
max_A = A.max()
print("\nMinimum value of matrix A:",min_A)
print("\nMaximum value of matrix A:",max_A)
 
#Create vector X (an array) with 4 random numbers
X = random.random(4)
print("\nVector X:\n",X)

#Create a function and pass vector X and matrix A in it
#In the new function multiply vector X with matrix A and assign the result to D
def mult(X,A):
    D = np.dot(X,A.T)
    return D
         
# Create a complex number Z with absolute and real parts != 0
Z = 3-2j
print("\nComplex number Z:",Z)

# Show its real and imaginary parts as well as it’s absolute value
Z_real = Z.real
Z_imag = Z.imag
Z_abs = np.absolute(Z)
print("\nReal part of Z:",Z_real)
print("\nImaginary part of Z:",Z_imag)
print("\nAbsolute value of Z:",Z_abs)

#Multiply result D with the absolute value of Z and record it to C
D = mult(X,A)
C = D*Z_abs
print("\nC:\n",C)

#Convert matrix B from a matrix to a string and overwrite B
B = str(B)
print("\nString B:\n%s"% B)
print("New type of B:",type(B))

#Display a text on the screen: ‘Your Name is done with HW2‘
print("\nSwetha Susan George is done with HW2")
