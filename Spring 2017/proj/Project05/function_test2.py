# Testing the get_shift function

from proj05 import get_shift

print("Testing the function: get_shift")

s = "Ji qnpjx yt jfy wji gjjyx."
s = s.upper()
ignore = ''
print("Cipher text:",s)
shift, max_ch = get_shift(s,ignore)
print("shift,max_ch:",shift,max_ch)
ignore += max_ch
print("ignore:",ignore)
shift, max_ch = get_shift(s,ignore)
print("shift,max_ch:",shift,max_ch)