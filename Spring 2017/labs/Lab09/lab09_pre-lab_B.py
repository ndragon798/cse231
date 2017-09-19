
M = {}
M[ "Joyce" ] = 7
M[ "Mike" ] = 12
M[ "Bea" ] = 9 

print( "M:", M )   

if "Bea" in M:
    A = M[ "Bea" ]
    print( "A:", A )
    
if "Joyce" in M:
    del M[ "Joyce" ]

print( "M:", M )   