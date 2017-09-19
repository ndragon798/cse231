
def total( start, end ):

    tot = 0

    for n in range(start,end):
        tot += n

    return tot

A = total( 0, 10 )

print( "Value of A:", A )            # Value of A: ____________

B = total( 8, 12 )

print( "Value of B:", B )            # Value of B: ____________

C = total( 15, 15 )

print( "Value of C:", C )            # Value of C: ____________

D = 3 * total( 4, 7 ) + 10

print( "Value of D:", D )            # Value of D: ____________

X = 5
E = total( 2*X, 12 )

print( "Value of E:", E )            # Value of E: ____________
