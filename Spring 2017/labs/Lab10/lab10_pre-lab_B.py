
S = { 10, 20, 30, 40 }
T = { 30, 40, 50 }
U = { 10, 30 }

B = S | T
print( "B:", B )                # B:

C = S.intersection( T )
print( "C:", C )                # C:

D = S & T
print( "D:", D )                # D:

F = S ^ T
print( "F:", F )                # F:

H = S - T
print( "H:", H )                # H:

I = S.issuperset( S )
print( "I:", I )                # I:

J = S.issuperset( T )
print( "J:", J )                # J:

K = S.issuperset( U )
print( "K:", K )                # K:

L = S > U
print( "L:", L )                # L:

M = U.issubset( S )
print( "M:", M )                # M:

N = U < S
print( "N:", N )                # N:
