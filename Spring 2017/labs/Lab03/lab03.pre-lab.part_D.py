
message = "Values {} and {}."

A = message.format( 25, -37 )

print( "A:", A )                         # A: _____________________

B = message.format( 1.25, "Zero" )

print( "B:", B )                         # B: _____________________

pattern = "|{:5d}| |{:4d}|"

C = pattern.format( 175, -93 )

print( "C:", C )                         # C: _____________________

pattern = "|{:>+5d}| |{:<-4d}|"

D = pattern.format( 175, -93 )

print( "D:", D )                         # D: _____________________

E = pattern.format( -87, 26 )

print( "E:", E )                         # E: _____________________

pi = 3.141592653589793

F = "{:.4f}".format( pi )

print( "F:", F )                         # F: _____________________

G = "{:8.4f}".format( pi )

print( "G:", G )                         # G: _____________________

min_flt = 2.2250738585072014e-308

H = "{:.4e}".format( min_flt )

print( "H:", H )                         # H: _____________________

I = "{:.4f}".format( min_flt )

print( "I:", I )                         # I: _____________________

max_flt = 1.7976931348623157e+308

J = "{:.4e}".format( max_flt )

print( "J:", J )                         # J: _____________________

K = "{:.4f}".format( max_flt )

print( "K:", K )                         # K: _____________________
