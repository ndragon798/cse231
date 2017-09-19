
from proj09 import read_data, find_cooccurance
print("Testing proj09 functions using pimpernel.txt")
try:
    fp = open("pimpernel.txt")
except FileNotFoundError:
    print("You need the file pimpernel.txt for this test.")

print("\nTesting read_data.")
print("Dictionary should be:\n  {'seek': {1, 2, 3}, 'everywhere': {3}, 'him': {1, 2, 3}, 'those': {3}, 'frenchies': {3}, 'they': {1, 2}, 'here': {1}, 'there': {2}}")

D = read_data(fp)
print("Dictionary D:\n",D)

print("\nTesting find_cooccurance.")
print("Test 1 should be: [1, 2, 3].")
print(find_cooccurance(D,"seek"))

print("\nTest 2 should be: [1, 2].")
print(find_cooccurance(D,"seek they"))

print("\nTest 3 should be: [1, 2, 3].")
print(find_cooccurance(D,"him seek"))

print("\nTest 4 should be: [1].")
print(find_cooccurance(D,"here"))
