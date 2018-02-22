
import numpy as np


def ThomasAlgo(a, b, c, d):
    '''
    Thomas Algorithm, a b c d can be NumPy array type or Python list type.
    refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    and to http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
    '''
    nf = len(d) # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
    for it in xrange(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1] 
        dc[it] = dc[it] - mc*dc[it-1]
        	    
    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in xrange(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc

# Matrix
a = [1.0] * 99 #first diagonal (upper)
c =[1.0] *99   #second diagonal (lower)
b= [-2.0] * 100 #main diagonal (mid)

d=[] #b from Ax=b #array

for r in range(101): #0-100
  h1= r+1 #to avoid division by zero error
  h = 1.0/h1
  h2 = h*h
  d.append(h2) #add the h2 inside the array b
d.pop(0)
print "n = ", len(d) ,"\n"
  

# Execute the function
print "x1 -x%s: (repectively)\n"%len(d)
print ThomasAlgo(a, b, c, d)
# Print the result
