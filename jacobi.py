'''https://austingwalters.com/jacobi-method/'''

import numpy as np
from scipy.linalg import solve

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)
    
    for i in range(n):
        x = (b - np.dot(R,x))/ D
    return x


def createMatrix(n):
    value = 1
    rows = 1
    cols = n-1
    a = np.tile(value, (rows,cols))

    z = np.zeros((n,n))
    z[np.arange(n), np.arange(n)] = -2 # diagonal is 1
    z[np.arange(cols), np.arange(cols) + 1] = 1 # first upper diagonal is 2
    z[np.arange(cols) + 1, np.arange(cols)] = a # first lower diagonal values
    
    return z

'''___Main___'''

A = createMatrix(30)

b=[] #b from Ax=b #array

for r in range(31): #0-6
  h1= r+1 #to avoid division by zero error
  h = 1.0/h1
  h2 = h*h
  b.append(h2) #add the h2 inside the array b

  

b.pop(0) #remove index[0] from array, in order to start with n=1


x = [0] * 30
n = 30

x = jacobi(A, b, x, n)

print "n = ", n

print "\n solving for (x1 - x%s) . . . \n"%len(x)
for elementx in solve(A, b):
    print elementx

