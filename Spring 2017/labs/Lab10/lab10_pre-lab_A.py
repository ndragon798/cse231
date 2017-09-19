
S = {900, 400, 700, 800}

A = 400 in S
print( "A:", A )                 # A:

item = 200
B = item not in S
print( "B:", B )                 # B:

print( "len(S):", len(S) )       # len(S):

S.add( 900 )
print( "S:", S )                 # S:

item = 400
S.discard( item )
print( "S:", S )                 # S:

print( "len(S):", len(S) )       # len(S):

