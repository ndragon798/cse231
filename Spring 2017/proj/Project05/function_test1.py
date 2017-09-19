# Testing get_char

from proj05 import get_char

print("Testing the function: get_char")
ch = 'H'
shift = 3
print("cipher-ch, plain-ch:",ch,shift,get_char(ch,shift))
shift = -3
print("cipher-ch, plain-ch:",ch,shift,get_char(ch,shift))
ch = 'A'
shift = -1
print("cipher-ch, plain-ch:",ch,shift,get_char(ch,shift))
ch = 'Z'
shift = 1
print("cipher-ch, plain-ch:",ch,shift,get_char(ch,shift))
shift = 0
print("cipher-ch, plain-ch:",ch,shift,get_char(ch,shift))