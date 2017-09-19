#####################################
# Computer Project #5
#
#Read in ciphered text
#Gets most common char and shift by that char
#Prints out deciphered text
#If text isn't readable then shift again by next most common char
#####################################
# Uncomment the following lines when you run the run_file tests
# so the input shows up in the output file.
#
# import sys
# def input( prompt=None ):
# 	if prompt != None:
# 		print( prompt, end="" )
# 	aaa_str = sys.stdin.readline()
# 	aaa_str = aaa_str.rstrip( "\n" )
# 	print( aaa_str )
# 	return aaa_str
	
import string  

def get_char(ch,shift):
	''' Function takes 2 parameters and returns the character after applying the shift'''
	#try to get chars based on the shift
	try:
		cipherTextChar = (string.ascii_uppercase.index(ch) + shift) % 26
		cipherTextChar=string.ascii_uppercase[cipherTextChar]
		return cipherTextChar #return the fixed character
	except Exception as e:
		return ch#returns white space or none alphachars
	
def get_shift(s,ignore):
	''' Function takes 2 parameters and returns the shift and the max most common character'''
	count_topletter=0
	topletter=''
	#replaces ignore chars in the cipher text with blank space so they cant be most common char
	for letters in ignore:
		s=s.replace(letters,'')
	s=s.replace(" ",'')#removes white space so that spaces cant be most common
	for chars in string.ascii_uppercase:#find the most common chars
		if (s.count(chars)>count_topletter):
			count_topletter=s.count(chars)
			topletter=chars
	max_ch=topletter
	#gets the shift based on the most common
	shift=string.ascii_uppercase.index('E')-string.ascii_uppercase.index(max_ch)
	return shift, max_ch #returns the shift and most common char
	
def output_plaintext(s,shift):
	''' Function takes 2 parameters and prints the plaintext of the caesar cypher'''
	word=''
	s=s.upper()
	#builds the word/phrase and prints it
	for letter in s:
		word=word+get_char(letter,shift)
	print(word)
		
def main():
	print("Cracking a Caesar cypher.")
  	#Read Input
	plaintext='no'
	cipher=input("Input cipher Text: ")
	cipher=cipher.upper()
	ignore=''
	#if it doesn't print to plaintext then it keeps looping
	while(plaintext=='no'):
		shift,max_ch=get_shift(cipher,ignore)
		ignore=ignore+max_ch
		output_plaintext(cipher,shift)
		plaintext=input("Is the plaintext readable as English? (yes/no): ")

if __name__ == "__main__": 
	main()

