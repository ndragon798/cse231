value = input( "Input value: " )
try:
    print( "Result =", end=" ")
    value = int(value)
    result = 20/value
    print( result, end=" " )
except ValueError:
    print( "Value Error", end=" " )
except ZeroDivisionError:
    print( "Zero Division Error", end=" " )
print( )