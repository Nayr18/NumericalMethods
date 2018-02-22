import numpy as np
import sys
import matrix5
import matrix10
import matrix100
import matrix200
import matrix500



def linearsolver(A,b):
  n = len(A) #size of matrix
  M = A #copy
  print "n= ",len(M)
 
  for elementb in b:
        print elementb 
  
  print "\n solving for (x1 - x%s) . . . \n"%len(b)

  i = 0

  
  for x in M:
    x.append(b[i])
    i += 1

  # the pivot searching for heigher value per column and row
  for k in range(n):
    for i in range(k,n):
      if abs(M[i][k]) > abs(M[k][k]):
        
        M[k], M[i] = M[i],M[k]
      else:  #else continue
        pass

    for j in range(k+1,n):
      q = float(M[j][k]) / M[k][k]
      for m in range(k, n+1):
        M[j][m] -=  q * M[k][m]
          
          
  x = [0 for i in range(n)]
  #elements arithmetic 

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  
  
  for elementx in x:
        print elementx 






#MAIN 
b=[] #b from Ax=b #array

for r in range(101): #0-50
  h1= r+1 #to avoid division by zero error
  h = 1.0/h1
  h2 = h*h
  b.append(h2) #add the h2 inside the array b


b.pop(0) #remove index[0] from array, in order to start with n=1


matrix = matrix100.main()


#function call
linearsolver(matrix, b)







