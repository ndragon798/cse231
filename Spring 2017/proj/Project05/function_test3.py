# Testing the output_plaintext function

from proj05 import output_plaintext

print("Testing the function: output_plaintext")
s = "Ji qnpjx yt jfy wji gjjyx."
s = s.upper()
print("Cipher text:",s)

shift = -5
output_plaintext(s,shift)