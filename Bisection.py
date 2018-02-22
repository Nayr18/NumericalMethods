
import math


def bisect( f, a, b, tol, maxiter ):
    """
    Usage: ( x, rate ) = bisect( f, a, b, tol, maxiter )
   
    """

    def sign( x ):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0

    x  = a
    fa = f( a )
    fb = f( b )

    if sign( fa ) == sign( fb ):
        print "Interval [%f,%f] may not contain a root" % ( a, b )

 

    k = 0

    while k <= maxiter:
        
        x = ( a + b ) / 2.0
        fx = f( x )
        
        print "%2d %18.11e %18.11e %18.11e " % ( k, a, b, x )
        k = k + 1


        if sign( fa ) == sign( fx ):
            a, fa = ( x, fx )
        else:
            b = x

    if k > maxiter:
        print "Error: exceeded %d iterations" % maxiter

  
    return ( x)


if __name__ == "__main__":
  

    # Maximum number of iterations

    maxiter = 100

    # Tolerance for all algorithms.  This value determines how accurate
    # the final estimate of the root will be.

    tol = math.pow(10,-6)

    # ---------- Define f(x) -------------

    def  f(x): return math.exp(x)-math.sin(x)

    a, b = ( 0.0, 2.0 )
    first_guess = ( a + b ) / 2.0

    print "************************************************************"
    print "Finding roots of e^x = sinx"
    print "************************************************************"

    x = bisect( f, a, b, tol, maxiter )
    print "root = ", x

