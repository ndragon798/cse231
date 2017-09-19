value = input( "Input value: " )
try:
    print( "Result =")
    value = int(value)
    result = 20/value
    print( result)
except ValueError:
    print( "Value Error")
except ZeroDivisionError:
    print( "Zero Division Error")
print( )