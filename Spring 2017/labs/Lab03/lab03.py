word = input("Enter a word: ")
oword=word
vowels='aeiou'
quitter=False
while quitter==False:
	if word.lower()=="quit":
		quitter=True
	else:
		if word[:1].lower() in vowels:
			word = word+"way"
			oword='"'+oword+'"'
			word='"'+word+'"'
			print(oword.ljust(14) ,"becomes",word.rjust(14))
			word=input("Enter a word:")
			oword=word
		else:
			while True:
				if word[:1].lower() in vowels:
					word = word+"ay"
					oword='"'+oword+'"'
					word='"'+word+'"'
					print(oword.ljust(14) ,"becomes",word.rjust(14))
					word=input("Enter a word:")
					oword=word
					break
				else:
					word=word[1:]+word[:1]
					