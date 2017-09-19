
# Laboratory Exercise #2 (Part D)
#
# Purpose:  compute the two roots of a quadratic equation.
#
# Import the math module to access function "math.sqrt()".

import math

A = float( input( "\nEnter the coefficient A: " ) )

B = float( input( "\nEnter the coefficient B: " ) )

C = float( input( "\nEnter the coefficient C: " ) )

print( "\nThe coefficients of the equation:\n" )
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )


# **** Replace the following with the calculations of the roots ****

root1 = (B*-1)+(math.sqrt((B**2)-4*A*C)/2*A)  # replace 0.0 with the quadratic formula
root2 = (B*-1)-(math.sqrt((B**2)-4*A*C)/2*A)


print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", root1 )
print( "  Root #2 = ", root2 )
