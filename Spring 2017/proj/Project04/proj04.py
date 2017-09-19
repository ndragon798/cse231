#####################################
# Computer Project #4
#
#Tell user about game
#Prompt user for word
#Turn words into dashes
#begin game
#turn guesses from dashes to letters in the word
#win or lose.
#####################################
#Loops through the phrase turns phrase to dashes
def gendashes(phrase):
	dashes=phrase
	for i in range(len(dashes)):
		#print(dashes[i])
		if dashes[i] != ' ':
			dashes=dashes.replace(dashes[i],'-')
	return dashes
#Replaces given letter in the dashl
def replacedashes(phrase,letter,dashl):
	if len(letter)<=1:
		dashes=dashl[0:phrase.find(letter)]+letter+dashl[phrase.find(letter)+1:]
		phrase=phrase.replace(letter," ",1)
		if phrase.find(letter) !=-1:
			#Don't know if you guys care or not but I'm gonna 
			#be using recursion a lot throughout this class
			#I really like recursion
			return replacedashes(phrase,letter,dashes)
		else:
			return dashes
	else:
		if letter == phrase:
			return phrase,True
		else:
			return dashl
#General game function
#Read in phrase dashes k and used

def game(phrase,dashes,k,used):
	#Check a win condition and lose conditions
	if phrase==dashes and k>=0:
		print("You won.")
	elif k==0:
		print("You lost")
		print("The word/phrase was: "+ phrase)
	else:
		#Read in guess
		guess=input("Guess a letter or whole word/phrase: ")
		#Error checking
		while guess.replace(' ','').isalpha() !=True:
			print("Only letters and spaces are allowed as input.")
			guess=input("Guess a letter or whole word/phrase: ")
		#Not nessisary error checking just to lazy to take it out as it was my first attempt 
		#at error checking before I found the method above
		try: 
			int(guess)
			print("Only letters and spaces are allowed as input.")
			#Suprise more recursion
			game(phrase,dashes,k,used)
		except Exception as e:
			guess=guess.lower()
			used=used+guess
			#if guess is equal to phrase win condition
			if guess == phrase:
				print("You won.")
				#if guess is in phrase but not equal to phrase
			elif guess in phrase:
				#More recursion to get the dashes removed from the var dashes
				dashes=replacedashes(phrase,guess,dashes)
				print("current: "+dashes)
				#Take away a turn
				k=k-1
				print(str(6-k)+" guesses so far out of 6: "+str(used))
				#Call the game function again 
				game(phrase,dashes,k,used)
			#all others
			else:
				#take away a turn
				k=k-1
				print("Letter not in phrase.")
				print("current: "+dashes)
				print(str(6-k)+" guesses so far out of 6: "+str(used))
				#Call the game function again
				game(phrase,dashes,k,used)
def startphrase():
	#reads in and error checks input
	phrase=input("Enter a word or phrase: ")
	while phrase.replace(' ','').isalpha() !=True:
		print("Error:only letters are allowed as input.")
		phrase=input("Enter a word or phrase: ")
	#turn phrase to lower
	phrase=phrase.lower()
	print("phrase: "+phrase)
	#turn the phrase to dashes
	dashes=gendashes(phrase)
	print("current: "+dashes)
	print("0 guesses so far out of 6: ")
	return phrase,dashes
#initial game explination
print("Hangman: guess letters until you can guess the whole word or phrase. In this game you get six tries.")
#get phrase and dashes from startphrase
phrase,dashes=startphrase()
#Start the game with 6 attempts
game(phrase,dashes,6,"")