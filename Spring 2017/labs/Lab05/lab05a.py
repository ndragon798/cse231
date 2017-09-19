def openfile():
	fileloc=("dictionary.txt")
	try:
		fp = open(fileloc)
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=openfile()
		return fp	
fp=openfile()
for word in fp:
	vowels=0
	if len(word)==8:
		if word[0].isupper()==False:
			for letter in word:
				if "a" in letter:
					vowels+=1
				elif 'e' in letter:
					vowels+=1
				elif 'i' in letter:
					vowels+=1
				elif 'o' in letter:
					vowels+=1
				elif 'u' in letter:
					vowels+=1
				elif 'y' in letter:
					vowels+=1
			if vowels==1 and 's' not in word:
				print(word)	