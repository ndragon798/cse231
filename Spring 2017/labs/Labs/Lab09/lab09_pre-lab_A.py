
def display( y ):
    
    x = 2
    print( "\nIn display, x:", x )
    print( "\nIn display, y:", y )
    
    # Here we print out the actual namespace
    # locals is the generic name of the current namepace
    # it is a "dictionarly", a data type we will study soon.
    # We use 'for' to iterate through the whole namespace
    # and print each item in the namespace.
    print( "\n\tNamespace for function display:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

def main():
    
    x = 6
    display( x+2 )

    print( "\nIn main, x:", x )

    print( "\n\tNamespace for function main:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

main()
