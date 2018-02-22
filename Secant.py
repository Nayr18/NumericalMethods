
import math
"""
* Variable Description:
* f			:	Given function
* [a, b]	:	End point values
* TOL		:	Tolerance
* NMAX		:	Max number of iterations
"""


def secant(f,x0,x1, TOL=0.001, NMAX=100):

	n=1
	while n<=NMAX:
		x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
		if x2-x1 < TOL:
			return x2
		else:
			x0 = x1
			x1 = x2
	return False


if __name__ == "__main__":
	
	def func(x):
	
		return (82944)*(math.pow(x,10)) - (118656)*(math.pow(x,3)) + (60292)*(math.pow(x,6))-(13133)*(math.pow(x,4))+(1189)*(math.pow(x,2))-36

	tol = math.pow(10,-4)
	#Invoking Secant Method
	res = secant(func,1,2)
	print res

