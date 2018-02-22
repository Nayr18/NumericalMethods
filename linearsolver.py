from numpy import *
from scipy.optimize import *

'''
    Docs for scipy.optimize : https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.fsolve.html
'''
def myFunction(z):
   x1 = z[0]
   x2 = z[1]
   x3 = z[2]

 
   F[0] = x1+x2+x3-2
   F[1] = pow(x1,2) +pow(x2,2)+ pow(x3,2) -6 
   F[2] = -1*(x1*x2*x3)-2
   

zGuess = array([1,0,1])
result = fsolve(myFunction,zGuess)

print result
